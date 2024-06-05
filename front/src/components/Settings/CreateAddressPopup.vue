<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление адреса</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Город</h5>
          <div class="inner-block">
            <MySelect v-if="this.cityMode === 'select'"
                      :options="this.cities"
                      @selectChanged="cityChanged">
            </MySelect>
            <MyInput v-if="this.cityMode === 'add'"
                     :placeholder="'Название города'"
                     :model-value="this.cityName"
                     @input="this.cityName = $event.target.value">
            </MyInput>

            <div class="switch-mode" v-if="this.cityMode === 'select'">
              <img class="switch-button-img"
                   src="@/assets/Add.svg"
                   alt="switch-mode"
                   @click="this.cityMode = 'add'">
            </div>

            <div class="switch-mode" v-if="this.cityMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Save.svg"
                   alt="switch-mode"
                   @click="createCity">
            </div>
            <div class="switch-mode" v-if="this.cityMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Back.svg"
                   alt="switch-mode"
                   @click="this.cityMode = 'select'">
            </div>
          </div>

          <h5 v-if="this.showStreetBlock">Улица</h5>
          <div v-if="this.showStreetBlock" class="inner-block">
            <MySelect v-if="this.streetMode === 'select'"
                      :options="this.streets"
                      @selectChanged="streetChanged">
            </MySelect>
            <MyInput v-if="this.streetMode === 'add'"
                     :placeholder="'Название улицы'"
                     :model-value="this.streetName"
                     @input="this.streetName = $event.target.value">
            </MyInput>

            <div class="switch-mode" v-if="this.streetMode === 'select'">
              <img class="switch-button-img"
                   src="@/assets/Add.svg"
                   alt="switch-mode"
                   @click="this.streetMode = 'add'">
            </div>

            <div class="switch-mode" v-if="this.streetMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Save.svg"
                   alt="switch-mode"
                   @click="createStreet">
            </div>
            <div class="switch-mode" v-if="this.streetMode === 'add'">
              <img class="switch-button-img"
                   src="@/assets/Back.svg"
                   alt="switch-mode"
                   @click="this.streetMode = 'select'">
            </div>
          </div>

          <div v-if="this.showNumberBlock" class="inner-block">
            <h5>Дом</h5>
            <MyInput :placeholder="'Номер дома'"
                     :model-value="this.houseNumber"
                     @input="this.houseNumber = $event.target.value">
            </MyInput>

            <h5>корпус</h5>
            <MyInput :placeholder="'Корпус'"
                     :model-value="this.houseCorpus"
                     @input="this.houseCorpus = $event.target.value">
            </MyInput>
          </div>

          <MyButton v-if="this.showNumberBlock" @click="save">
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
      cityMode: 'select',
      cities: [],
      selectedCity: -1,
      cityName: '',

      showStreetBlock: false,
      streetMode: 'select',
      streets: [],
      selectedStreet: -1,
      streetName: '',

      showNumberBlock: false,
      houseNumber: '',
      houseCorpus: '',
    }
  },
  beforeMount() {
    this.loadCities();
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async loadCities() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/city/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.cities = response.data
      } catch (e) {
        alert(`Города: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    async loadStreets() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/city/${this.selectedCity}/streets`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.streets = response.data
      } catch (e) {
        alert(`Улицы: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    cityChanged(pk) {
      this.selectedCity = pk
      this.showStreetBlock = true
      this.loadStreets()
    },
    streetChanged(pk) {
      this.selectedStreet = pk
      this.showNumberBlock = true
    },
    async createCity() {
      try {
        await axios.post(
            `${this.baseURL}/api/v1/city/create/`,
            {
              name: this.cityName,
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
      } catch (e) {
        alert(`Ошибка создания города\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
      this.loadCities()
      this.cityMode = 'select'
    },
    async createStreet() {
      try {
        await axios.post(
            `${this.baseURL}/api/v1/street/create/`,
            {
              city: this.selectedCity,
              name: this.streetName,
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
      } catch (e) {
        alert(`Ошибка создания улицы\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
      this.loadStreets()
      this.streetMode = 'select'
    },
    async save() {
      try {
        await axios.post(
            `${this.baseURL}/api/v1/address/create/`,
            {
              street: this.selectedStreet,
              number: this.houseNumber,
              corpus: this.houseCorpus
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

      this.cityMode = 'select'
      this.selectedCity = -1
      this.cityName = ''
      this.showStreetBlock = false
      this.streetMode = 'select'
      this.selectedStreet = -1
      this.streetName = ''
      this.showNumberBlock = false
      this.houseNumber = ''
      this.houseCorpus = ''
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
  min-height: 150px;
  width: 550px;
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