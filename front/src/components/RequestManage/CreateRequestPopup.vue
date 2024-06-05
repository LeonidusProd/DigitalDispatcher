<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3 v-if="this.residentMode === 'select'">Создание заявки</h3>
          <h3 v-if="this.residentMode === 'add'">Создание жителя</h3>
          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>
        <div class="down-block">
          <h5 v-if="this.residentMode === 'select'">Текст обращения:</h5>
          <MyTextarea :placeholder="'Причина обращения жителя'"
                      :model-value="this.requestText"
                      @input="this.requestText = $event.target.value"
                      class="request-reason"
                      v-if="this.residentMode === 'select'">
          </MyTextarea>

          <h5 v-if="this.residentMode === 'select'">Адрес:</h5>
          <MySelect :options="addresses"
                    @selectChanged="addressChanged"
                    v-if="this.residentMode === 'select'">
          </MySelect>

          <div v-if="this.residentMode === 'select'" class="inner-block">
            <h5>Квартира</h5>
            <MyInput :placeholder="'№ квартиры'"
                     :model-value="this.apartment"
                     @input="this.apartment = $event.target.value"
                     class="apart-input"
                     type="number">
            </MyInput>
          </div>

          <h5 v-if="this.residentMode === 'select'">Житель:</h5>
          <div class="inner-block">
            <MySelect v-if="this.residentMode === 'select'"
                      :options="this.residents"
                      @selectChanged="residentChanged">
            </MySelect>

            <div class="switch-mode" v-if="this.residentMode === 'select'">
              <img class="switch-button-img"
                   src="@/assets/Add.svg"
                   alt="switch-mode"
                   @click="this.residentMode = 'add'">
            </div>

            <div class="switch-mode" v-if="this.residentMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Save.svg"
                   alt="switch-mode"
                   @click="createResident">
            </div>
            <div class="switch-mode" v-if="this.residentMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Back.svg"
                   alt="switch-mode"
                   @click="this.residentMode = 'select'">
            </div>
          </div>

          <div class="add-resident-form" v-if="this.residentMode === 'add'">
            <h5>Фамилия:</h5>
            <MyInput :placeholder="'Фамилия жителя'"
                     :model-value="this.residentSurname"
                     @input="this.residentSurname = $event.target.value">
            </MyInput>

            <h5>Имя:</h5>
            <MyInput :placeholder="'Имя жителя'"
                     :model-value="this.residentName"
                     @input="this.residentName = $event.target.value">
            </MyInput>

            <h5>Отчество:</h5>
            <MyInput :placeholder="'Отчество жителя'"
                     :model-value="this.residentPatronymic"
                     @input="this.residentPatronymic = $event.target.value">
            </MyInput>

            <h5>Номер телефона:</h5>
            <MyInput :placeholder="'Номер телефона жителя'"
                     :model-value="this.residentPhone"
                     @input="this.residentPhone = $event.target.value">
            </MyInput>
          </div>


          <my-button v-if="this.residentMode === 'select'"
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
import MyTextarea from "@/components/UI/MyTextarea.vue";
import MyInput from "@/components/UI/MyInput.vue";

export default {
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  components: {MyInput, MyTextarea, MyButton, MySelect},
  data() {
    return {
      requestText: '',

      addresses: [],
      selectedAddress: -1,
      apartment: '',

      residentMode: 'select',
      residents: [],
      selectedResident: -1,

      residentName: '',
      residentSurname: '',
      residentPatronymic: '',
      residentPhone: '',
    }
  },
  computed: {
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      baseURL: state => state.main.baseURL,
    }),
  },
  mounted() {
    this.loadAddresses()
    this.loadResidents()
  },
  methods: {
    async loadAddresses() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/address/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.addresses = response.data
      } catch (e) {
        alert(`Адреса: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    addressChanged(pk) {
      this.selectedAddress = pk
    },

    async loadResidents() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/resident/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.residents = response.data
      } catch (e) {
        alert(`Жители: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    residentChanged(pk) {
      this.selectedResident = pk
    },

    async createResident() {
      if (this.residentName !== '' && this.residentSurname !== '' && this.residentPhone !== '') {
        try {
          await axios.post(
              `${this.baseURL}/api/v1/resident/create/`,
              {
                name: this.residentName,
                surname: this.residentSurname,
                patronymic: this.residentPatronymic,
                phone: this.residentPhone
              },
              {
                headers: {
                  'Authorization': `Token ${localStorage.getItem('auth_token')}`
                }
              }
          )
        } catch (e) {
          alert(`Ошибка создания жителя\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

          this.$emit('close')
        }
        this.loadResidents()
        this.residentMode = 'select'

        this.residentName = ''
        this.residentSurname = ''
        this.residentPatronymic = ''
        this.residentPhone = ''
      }
    },

    async save() {
      if (this.requestText !== '' && this.selectedResident !== -1 && this.selectedAddress !== -1) {
        console.log(this.requestText)
        console.log(this.selectedResident)
        console.log(this.selectedAddress)
        try {
          await axios.post(
              `${this.baseURL}/api/v1/request/create/`,
              {
                text: this.requestText,
                status: 1,
                resident: this.selectedResident,
                address: this.selectedAddress,
                apartment: Number(this.apartment)
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

          this.$emit('close')
        }

        this.$emit('save')

        this.selectedResident = -1
        this.selectedAddress = -1
        this.requestText = ''
        this.apartment = ''
      }
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

.request-reason {
  height: 150px;
  width: 400px;
}

.inner-block {
  display: flex;
  flex-direction: row;
  width: 100%;
  gap: 10px;
}

.switch-mode {
  height: 37px;
  min-width: 37px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.switch-mode:hover {
  height: 37px;
  min-width: 37px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.switch-button-img {
  width: 100%;
}

.apart-input {
  width: 150px;
}
</style>