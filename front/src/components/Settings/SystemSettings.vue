<template>
  <div class="inside-container" v-if="loadSucsess">
    <div class="left-side">
      <h3>Токен бота приёма заявок</h3>
      <my-input class="bot-token-input"
                :placeholder="'Вставьте токен бота'"
                :model-value="resBotToken"
                @input="resBotToken = $event.target.value">
      </my-input>

      <h3>Токен бота распределения задач</h3>
      <my-input class="bot-token-input"
                :placeholder="'Вставьте токен бота'"
                :model-value="staffBotToken"
                @input="staffBotToken = $event.target.value">
      </my-input>
    </div>

    <div class="right-side">
      <my-button @click="saveSettings"
                 class="save-button">
        Сохранить
      </my-button>
    </div>
  </div>
  <div class="alert" v-else>
    <h1>Ошибка загрузки данных, попробуйте ещё раз позже</h1>
    <h4>Ошибка: {{ errorCode }}</h4>
    <h4>Сообщение: {{ errorMessage }}</h4>
  </div>
</template>

<script>

import {defineComponent} from "vue";
import MyInput from "@/components/UI/MyInput.vue";
import MySelect from "@/components/UI/MySelect.vue";
import MyButton from "@/components/UI/MyButton.vue";
import axios from "axios";
import {mapState} from "vuex";

export default defineComponent({
  components: {MyButton, MySelect, MyInput},
  data() {
    return {
      loadSucsess: true,
      errorMessage: '',
      errorCode: 0,

      resBotToken: 0,
      staffBotToken: 0
    }
  },
  beforeMount() {
    this.loadSettings()
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async saveSettings() {
      try {
        await axios.put(
            `${this.baseURL}/api/v1/bottokens/manage/1`,
            {
              residentBotToken: this.resBotToken,
              staffBotToken: this.staffBotToken
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
      } catch (e) {
        console.log(e)
        alert(`Ошибка сохранения\n
        Ошибка: ${e.response.status}\n
        Сообщение: ${e.response.data.detail}`)
      }

    },
    async loadSettings() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/bottokens/manage/1`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.resBotToken = response.data.residentBotToken
        this.staffBotToken = response.data.staffBotToken
      } catch (e) {
        this.errorMessage = e.response.data.detail
        this.errorCode = e.response.status

        this.loadSucsess = false
      }

    }
  }
})
</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 100%;
  width: 100%;
}
.left-side {
  width: 48%;
  display: flex;
  flex-direction: column;
  justify-content: start;
}
.right-side {
  width: 48%;
  display: flex;
  flex-direction: column;
  justify-content: end;
  align-items: end;
}
.bot-token-input {
  margin-bottom: 10px;
  height: 40px;
}
.save-button {
  width: 200px;
}
</style>