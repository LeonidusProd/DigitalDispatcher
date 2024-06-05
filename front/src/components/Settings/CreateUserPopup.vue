<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление пользователя</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Логин</h5>
          <MyInput :placeholder="'Логин'"
                   :model-value="this.login"
                   @input="this.login = $event.target.value">
          </MyInput>

          <h5>Пароль</h5>
          <MyInput :placeholder="'Пароль'"
                   :model-value="this.password"
                   @input="this.password = $event.target.value">
          </MyInput>

          <h5>Роль</h5>
          <MySelect :options="this.roles"
                    @selectChanged="roleChanged">
          </MySelect>

          <h5 v-if="showEmploeesSelect">Сотрудник</h5>
          <MySelect v-if="showEmploeesSelect"
                    :options="this.employees"
                    @selectChanged="employeeChanged">
          </MySelect>

          <MyButton @click="save">
            Сохранить
          </MyButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MySelect from "@/components/UI/MySelect.vue";
import MyInput from "@/components/UI/MyInput.vue";
import axios from "axios";
import {mapState} from "vuex";

export default {
  components: {MyButton, MySelect, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      login: '',
      password: '',
      selectedRole: -1,
      roles: [
        {pk: 1, name: 'Диспетчер'},
        {pk: 2, name: 'Бот'},
        {pk: 3, name: 'Администратор'},
      ],
      showEmploeesSelect: false,
      selectedEmployee: -1,
      employees: []
    }
  },
  beforeMount() {
    this.loadEmployees()
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async loadEmployees() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/employee/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.employees = response.data
      } catch (e) {
        alert(`Сотрудники: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    roleChanged(pk) {
      this.selectedRole = pk
      if (pk === 1 || pk === 3) {
        this.showEmploeesSelect = true
      } else if (pk === 2) {
        this.showEmploeesSelect = false
      }
    },
    employeeChanged(pk) {
      this.selectedEmployee = pk
    },
    async save() {
      if (this.login !== '' && this.password !== '' && this.selectedRole !== -1) {
        if (this.selectedRole === 1 && this.selectedEmployee !== -1) {
          try {
            await axios.post(
                `${this.baseURL}/api/v1/user/create/`,
                {
                  username: this.login,
                  password: this.password,
                  is_staff: true,
                  first_name: this.employees[this.selectedEmployee - 1].empl_name,
                  last_name: this.employees[this.selectedEmployee - 1].empl_surname
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
        } else if (this.selectedRole === 2) {
          try {
            await axios.post(
                `${this.baseURL}/api/v1/user/create/`,
                {
                  username: this.login,
                  password: this.password,
                  is_staff: true,
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
        } else if (this.selectedRole === 3 && this.selectedEmployee !== -1) {
          try {
            await axios.post(
                `${this.baseURL}/api/v1/user/create/`,
                {
                  username: this.login,
                  password: this.password,
                  is_superuser: true,
                  first_name: this.employees[this.selectedEmployee - 1].empl_name,
                  last_name: this.employees[this.selectedEmployee - 1].empl_surname
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
        }
      }

      this.$emit('save')
      this.login = ''
      this.password = ''
      this.selectedRole = -1
      this.selectedEmployee = -1
      this.showEmploeesSelect = false
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
  z-index: 1000;
}

.dialog-content {
  margin: auto;
  background: white;
  border-radius: 12px;
  min-height: 320px;
  width: 500px;
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