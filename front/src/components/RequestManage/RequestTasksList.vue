<template>
  <h5 v-if="requestTasks.length === 0">Нет назначенных задач</h5>
  <div v-else class="task-cards">
    <div class="task-card-headers">
      <span class="task-card-empl">Сотрудник</span>
      <span class="task-card-task">Задача</span>
      <span class="task-card-stat">Статус</span>
    </div>
    <div class="tasks-list custom-scroll">
      <RequestTaskCard v-for="task in this.requestTasks"
                       :task-data="task"
                       @deleteTask="$emit('deleteTask')">
      </RequestTaskCard>
    </div>
  </div>
</template>

<script>
import {mapMutations, mapState} from "vuex";
import axios from "axios";
import RequestTaskCard from "@/components/RequestManage/RequestTaskCard.vue";

export default {
  components: {RequestTaskCard},
  data() {
    return {
      requestTasks: [],
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
      this.loadRequestTasks()
    }
  },
  methods: {
    ...mapMutations({
      setActiveRequestId: "requests/setActiveRequestId"
    }),
    async loadRequestTasks() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/request/${this.activeRequestId}/tasks`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))

        this.requestTasks = response.data
      } catch (e) {
        alert(`Заявка № ${this.activeRequestId}: Задачи: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.setActiveRequestId(-1)
      }
    },
  },
}

</script>

<style scoped>
.task-cards {
  height: 84%;
}
.tasks-list {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding-right: 3px;
  margin-top: 3px;
  border-radius: 12px;
  height: 140px;
}
.task-card-empl {
  width: 30%
}
.task-card-task {
  width: 44%
}
.task-card-stat {
  width: 21%
}
.task-card-headers {
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  width: 99%;
  height: 32px;
  display: flex;
  background-color: rgb(109, 197, 195, 0.4);
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
</style>