<template>
  <div class="card">
    <span>{{ this.name }}</span>

    <div class="delete-button">
      <img class="delete-button-img"
           src="@/assets/Close.svg"
           alt="del-sevice"
           @click="deleteElement">
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {mapState} from "vuex";

export default {
  props: ['pk', 'name', 'modelName'],
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async deleteElement() {
      try {
        await axios.delete(
            `${this.baseURL}/api/v1/${this.modelName}/delete/${this.pk}`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
        this.$emit('deleteElement')
      } catch (e) {
        alert(`Ошибка удаления записи\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)
      }
    }
  }
}
</script>

<style scoped>
.card {
  border-radius: 10px;
  border: none;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  flex-direction: row;
  background-color: rgb(139, 182, 177, 0.4);
  justify-content: space-between;
}

.delete-button {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.delete-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.delete-button-img {
  width: 100%;
}
</style>