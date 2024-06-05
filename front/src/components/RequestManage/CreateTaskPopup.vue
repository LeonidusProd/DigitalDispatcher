<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Создание задачи</h3>
          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>
        <div class="down-block">
          <h5>Задача:</h5>
          <MySelect :options="services"
                    @selectChanged="serviceChanged"></MySelect>
          <h5 v-if="showEmploeesSelect">Сотрудник:</h5>
          <MySelect v-if="showEmploeesSelect"
                    :options="employees"
                    @selectChanged="employeeChanged">
          </MySelect>

          <my-button v-if="showSaveButton"
                     @click="save">
            Сохранить
          </my-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
import axios from "axios";
import MySelect from "@/components/UI/MySelect.vue";
import MyButton from "@/components/UI/MyButton.vue";

export default {
  props: {
    show: {
      type: Boolean,
      default: false
    },
    requestOfficePk: [String]
  },
  components: {MyButton, MySelect},
  data() {
    return {
      services: [],
      selectedService: -1,

      employees: [],
      selectedEmployee: -1,
      showEmploeesSelect: false,

      showSaveButton: false,
    }
  },
  computed: {
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      baseURL: state => state.main.baseURL,
    }),
  },
  mounted() {
    this.loadServices()
  },
  methods: {
    async loadServices() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/service/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.services = response.data
      } catch (e) {
        alert(`Задачи: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    async loadEmployees() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/service/employees/`,
            {
              params: {
                'position_pk': this.selectedService,
                'office_pk': this.requestOfficePk
              },
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        console.log(response)
        this.employees = response.data
      } catch (e) {
        alert(`Сотрудники: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    serviceChanged(pk) {
      this.selectedService = pk
      this.loadEmployees()
      this.showEmploeesSelect = true
    },
    employeeChanged(pk) {
      this.selectedEmployee = pk
      this.showSaveButton = true
    },
    async save() {
      try {
        await axios.post(
            `${this.baseURL}/api/v1/task/create`,
            {
              request: this.activeRequestId,
              employee: this.selectedEmployee,
              service: this.selectedService,
              status: 1
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
      } catch (e) {
        alert(`Ошибка сохранения\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }

      this.$emit('save')

      this.selectedService = -1
      this.selectedEmployee = -1
      this.showEmploeesSelect = false
      this.showSaveButton = false
    }
  },
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgb(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}
.dialog-content {
  margin: auto;
  background: white;
  border-radius: 12px;
  height: 320px;
  width: 400px;
  padding: 20px;
  display: flex;
}
.create-task-content {
  width: 100%;
  background: rgb(169, 168, 159, 0.2);
  border-radius: 10px;
  padding: 10px;
}
.up-block {
  height: 30px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
}
.down-block {
  height: 90%;
  width: 100%;
  padding: 20px;
}
.close-dialog-button {
  height: 30px;
  width: 30px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}
.close-dialog-button:hover {
  height: 30px;
  width: 30px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}
.close-dialog-button-img {
  width: 100%;
}
</style>