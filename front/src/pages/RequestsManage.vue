<template>
  <div class="container">
    <div class="left-side-menu">
      <div class="up-block">
        <div class="logo-block">
          <img class="logo-img" src="@/assets/Лого%20текст%20снизу.svg" alt="logo">
        </div>
        <div class="menu-block">
          <MyButton @click="changeSection('new')"
                    :class="{'active-button':this.activeSection === 'new'}">
            Новые заявки
          </MyButton>
          <MyButton @click="changeSection('active')"
                    :class="{'active-button':this.activeSection === 'active'}">
            Активные заявки
          </MyButton>
          <MyButton @click="this.showRequestDialog = true">
            Создать заявку
          </MyButton>
          <CreateRequestPopup :show="this.showRequestDialog"
                              @close="this.showRequestDialog = false"
                              @save="saveRequest">
          </CreateRequestPopup>
        </div>
      </div>
      <div class="down-block">
        <MyButton @click="this.$router.push('/settings')" v-if="showSettingsButton">
          Настройки
        </MyButton>
        <MyButton @click="loguot">
          Выход
        </MyButton>
      </div>
    </div>

    <div class="workspace">
      <div class="requests-list">
        <RequestsList :key="requestsListKey"
                      :requests=this.requestsList
                      :request-list-landing="requestListLanding"
                      @reload="loadRequests">
        </RequestsList>
      </div>

      <div class="request-card">
        <h4 v-if="this.activeRequestId === -1">Ни одна заявка не выбрана</h4>
        <RequestCard v-else
                     :key="this.activeRequestId"
                     @closeRequest="loadRequests">
        </RequestCard>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import axios from "axios";
import {mapMutations, mapState} from "vuex";
import RequestsList from "@/components/RequestManage/RequestsList.vue";
import RequestCard from "@/components/RequestManage/RequestCard.vue";
import CreateRequestPopup from "@/components/RequestManage/CreateRequestPopup.vue";
import CreateTaskPopup from "@/components/RequestManage/CreateTaskPopup.vue";

export default {
  components: {CreateTaskPopup, CreateRequestPopup, RequestCard, RequestsList, MyButton},
  data() {
    return {
      activeSection: 'new',

      requestListLanding: 'Новые заявки',
      requestsListKey: 1,
      requestsList: [],

      showRequestDialog: false,

      showSettingsButton: false
    }
  },
  computed: {
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      baseURL: state => state.main.baseURL,
    }),
  },
  mounted() {
    this.checkUserRole()
    this.loadRequests()
  },
  methods: {
    ...mapMutations({
      setActiveRequestId: "requests/setActiveRequestId"
    }),
    changeSection(section) {
      this.activeSection = section
      this.loadRequests()
      this.setActiveRequestId(-1)
    },
    loadRequests() {
      if (this.activeSection === 'new') {
        this.requestListLanding = 'Новые заявки'
        this.loadNew()
      } else if (this.activeSection === 'active') {
        this.requestListLanding = 'Активные заявки'
        this.loadActive()
      }

      this.requestsListKey += 1
    },
    async loadNew() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/requests/new`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.requestsList = response.data
      } catch (e) {
        alert(`Новые заявки: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.requestsList = []
      }
    },
    async loadActive() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/requests/active`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.requestsList = response.data
      } catch (e) {
        alert(`Активные заявки: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.requestsList = []
      }
    },
    saveRequest() {
      this.loadRequests()
      this.showRequestDialog = false
    },
    async loguot() {
      try {
        await axios.post(
            `${this.baseURL}/auth/token/logout`,
            {},
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
        localStorage.removeItem('auth_token');
        localStorage.removeItem('user_role');

        this.$router.push('/');
      } catch (e) {
        alert(`Ошибка выхода\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)
      }
    },
    checkUserRole() {
      if (localStorage.getItem('user_role') === 'admin') {
        this.showSettingsButton = true
      }
    },
  },
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  min-height: 400px;
  height: 94vh;
}

.left-side-menu {
  background-color: rgb(169, 168, 159, 0.2);
  width: 20%;
  padding: 10px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.logo-block {
  text-align: center;
}

.logo-img {
  width: 50%;
}

.down-block {
  width: 100%;
}

.workspace {
  background-color: rgb(169, 168, 159, 0.2);
  width: 79%;
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-radius: 20px;
}

.requests-list {
  width: 35%;
  border: 1px;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px 10px 15px;
}

.request-card {
  width: 64%;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px;
}

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>