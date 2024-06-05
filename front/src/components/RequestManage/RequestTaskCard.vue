<template>
  <div class="task-card">
    <span class="task-card-empl">{{ taskData.employee }}</span>
    <span class="task-card-task">{{ taskData.task }}</span>
    <span class="task-card-stat">{{ taskData.status }}</span>
    <div class="delete-task-button">
      <img class="delete-task-button-img"
           src="@/assets/Close.svg"
           alt="del-task"
           @click="deleteTask(taskData.pk)">
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
import axios from "axios";

export default {
  props: ['taskData'],
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    }),
  },
  methods: {
    async deleteTask(pk) {
      try {
        await axios.delete(
            `${this.baseURL}/api/v1/task/delete/${pk}`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )

        this.$emit('deleteTask')
      } catch (e) {
        alert(`Ошибка удаления задачи\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)
      }
    }
  },
}
</script>

<style scoped>
.task-card {
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
}
.delete-task-button {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}
.delete-task-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}
.delete-task-button-img {
  width: 100%;
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
</style>