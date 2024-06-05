<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление сотрудника</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <div class="fields-block">
            <div class="inner-block">
              <h5>Фамилия</h5>
              <MyInput :placeholder="'Фамилия'"
                       :model-value="this.surname"
                       @input="this.surname = $event.target.value">
              </MyInput>

              <h5>Имя</h5>
              <MyInput :placeholder="'Имя'"
                       :model-value="this.name"
                       @input="this.name = $event.target.value">
              </MyInput>

              <h5>Отчество</h5>
              <MyInput :placeholder="'Отчество'"
                       :model-value="this.patronymic"
                       @input="this.patronymic = $event.target.value">
              </MyInput>

              <h5>Номер телефона</h5>
              <MyInput :placeholder="'Номер телефона'"
                       :model-value="this.phone"
                       @input="this.phone = $event.target.value"
                       type="phone">
              </MyInput>
            </div>

            <div class="inner-block">
              <h5>Электронная почта</h5>
              <MyInput :placeholder="'Электронная почта'"
                       :model-value="this.email"
                       @input="this.email = $event.target.value"
                       type="email">
              </MyInput>

              <h5>Управляющая компания</h5>
              <MySelect :options="this.offices"
                        @selectChanged="officeChanged">
              </MySelect>

              <h5>Должность</h5>
              <MySelect :options="this.positions"
                        @selectChanged="positionChanged">
              </MySelect>

              <h5>Telegram ID</h5>
              <MyInput :placeholder="'Telegram ID'"
                       :model-value="this.tgId"
                       @input="this.tgId = $event.target.value">
              </MyInput>
            </div>
          </div>

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
      surname: '',
      name: '',
      patronymic: '',
      phone: '',
      email: '',
      selectedOffice: -1,
      offices: [],
      selectedPosition: -1,
      positions: [],
      tgId: '',
    }
  },
  beforeMount() {
    this.loadOffices();
    this.loadPositions();
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async loadOffices() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/office/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.offices = response.data
      } catch (e) {
        alert(`УК: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    async loadPositions() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/position/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.positions = response.data
      } catch (e) {
        alert(`Должности: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    officeChanged(pk) {
      this.selectedOffice = pk
    },
    positionChanged(pk) {
      this.selectedPosition = pk
    },
    async save() {
      if (this.surname !== '' && this.name !== '' && this.patronymic !== '' &&
          this.phone !== '' && this.email !== '' && this.selectedOffice !== -1 &&
          this.selectedPosition !== -1 && this.tgId !== '') {
        try {
          await axios.post(
              `${this.baseURL}/api/v1/employee/create/`,
              {
                surname: this.surname,
                name: this.name,
                patronymic: this.patronymic,
                phone: this.phone,
                email: this.email,
                office: this.selectedOffice,
                position: this.selectedPosition,
                tg_id: this.tgId,
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
        this.surname = ''
        this.name = ''
        this.patronymic = ''
        this.phone = ''
        this.email = ''
        this.selectedOffice = -1
        this.offices = []
        this.selectedPosition = -1
        this.positions = []
        this.tgId = ''
      }
    },
  }
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
  min-height: 350px;
  width: 700px;
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

.fields-block {
  display: flex;
  flex-direction: row;
  gap: 20px;
  width: 100%;
}

.inner-block {
  display: flex;
  flex-direction: column;
  width: 100%;
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