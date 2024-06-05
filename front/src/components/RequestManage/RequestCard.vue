<template>
  <h4>Информация о заявке № {{ activeRequestId }}</h4>

  <div class="request-card-content">
    <div class="request-card-up">
      <div class="request-card-info-block custom-scroll">
              <span>
                <b>Сообщение жителя:</b><br>
                {{ requestInfo }}
              </span>
        <span>
          <b>Дата:</b> {{ requestDate.split(' ')[0] }} в {{ requestDate.split(' ')[1] }}
        </span>
        <span><b>Статус:</b> {{ requestStatus }}</span>
        <span><b>Житель:</b> {{ requestResident }}</span>
        <span><b>ЖК:</b> {{ requestComplex }}</span>
        <span><b>Адрес:</b> {{ requestAddress }}</span>

        <MyButton @click="closeRequest"
                  class="close-task-button">
          Закрыть заявку
        </MyButton>
      </div>
      <div class="request-card-photo-block">
        <b>Прикреплённая фотография:</b><br>
        <h6 v-if="requestPhoto === ''">Житель не прикрепил фотографию</h6>
        <div v-else class="request-photo">
          <img :src="requestPhoto" alt="problem-photo">
        </div>

      </div>
    </div>

    <div class="request-card-tasks-block" id="request_card_tasks_block">
      <div class="tasks-list-block">
        <h4>Назначенные задачи</h4>
        <RequestTasksList :key="taskListKey"
                          @deleteTask="taskListKey += 1">
        </RequestTasksList>

        <CreateTaskPopup
            :show="this.showDialog"
            :request-office-pk="this.requestOfficePk"
            @close="this.showDialog = false"
            @save="saveTask">
        </CreateTaskPopup>
      </div>
      <div class="tasks-button-block">
        <MyButton @click="this.showDialog = true"
                  class="create-task-button">
          Создать задачу
        </MyButton>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import {mapMutations, mapState} from "vuex";
import axios from "axios";
import RequestTasksList from "@/components/RequestManage/RequestTasksList.vue";
import CreateTaskPopup from "@/components/RequestManage/CreateTaskPopup.vue";

export default {
  components: {CreateTaskPopup, RequestTasksList, MyButton},
  data() {
    return {
      requestInfo: '',
      requestDate: '0 0',
      requestStatus: '',
      requestResident: '',
      requestAddress: '',
      requestPhoto: '',
      requestComplex: '',
      requestOfficePk: '',

      showDialog: false,

      taskListKey: 1,
    }
  },
  computed: {
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      baseURL: state => state.main.baseURL,
    }),
  },
  mounted() {
    if (this.activeRequestId !== -1) {
      this.loadRequestData()
    }
  },
  methods: {
    ...mapMutations({
      setActiveRequestId: "requests/setActiveRequestId"
    }),
    async loadRequestData() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/request/${this.activeRequestId}`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))

        this.requestInfo = response.data.info
        this.requestDate = response.data.date
        this.requestStatus = response.data.status_name
        this.requestResident = response.data.resident
        this.requestAddress = response.data.address
        if (response.data.photo) {
          this.requestPhoto = response.data.photo
        }
        this.requestComplex = response.data.complex
        this.requestOfficePk = response.data.office_id

      } catch (e) {
        alert(`Заявка № ${this.activeRequestId}: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.setActiveRequestId(-1)
        // this.$emit('loadError')
      }
    },
    async closeRequest() {
      try {
        const response = (await axios.put(
            `${this.baseURL}/api/v1/request/${this.activeRequestId}`,
            {
              status: 4
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.$emit('closeRequest')
      } catch (e) {
        alert(`Заявка № ${this.activeRequestId}: Ошибка закрытия заявки\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)
      }

      this.setActiveRequestId(-1)
    },
    saveTask() {
      this.taskListKey += 1
      this.showDialog = false
    },
  },
}
</script>

<style scoped>
.card-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.request-card-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 94%;
}

.request-card-up {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 49%;
}

.request-card-info-block {
  width: 49%;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.request-card-photo-block {
  width: 49%;
}

.request-photo {
  width: 95%;
  height: 95%;
  display: flex;
  vertical-align: middle;
  border-radius: 11px;
  overflow: hidden;
}

.request-photo img {
  width: 100%;
  height: 100%;
  border-radius: 11px;
  object-fit: cover;
}

.request-card-tasks-block {
  height: 49%;
  max-height: 49%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.create-task-button {
  width: 200px;
}

.custom-scroll::-webkit-scrollbar {
  width: 5px;
}

.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
  border-radius: 6px;
}

.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}

.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.tasks-list-block {
  display: flex;
  flex-direction: column;
  height: 80%;
}

.tasks-button-block {
  height: 19%;
  display: flex;
  flex-direction: row;
}
</style>