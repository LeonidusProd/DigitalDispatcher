<template>
  <div class="header-block">
    <h2>Укажите свой адрес</h2>

    <h6>Для начала укажите свой адрес. Выберите из выпадающих списков жилой комплекс и свой дом.</h6>

    <h6>Также можете указать номер квартиры. Это поможет быстрее найти вас.</h6>
  </div>

  <div class="step-content-block">
    <h5>Жилой комплекс</h5>
    <MySelect :options="complexes"
              @selectChanged="complexChanged">

    </MySelect>

    <h5 v-if="addressesVisiable">Адрес дома</h5>
    <MySelect :options="addresses"
              @selectChanged="addressChanged"
              v-if="addressesVisiable">

    </MySelect>

    <div class="apartment-group" v-if="addressesVisiable">
      <h5>Номер квартиры</h5>

    </div>
    <MyInput class="apartment-field"
             type="number"
             :model-value="apartmentNumber"
             @input="apartmentNumber = $event.target.value">
    </MyInput>

  </div>

  <div class="buttons-block" v-if="nextStepVisiable">
    <MyButton class="next-step-or-save"
              @click="nextStep">
      <h4>Следующий шаг</h4>
    </MyButton>
  </div>


</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MySelect from "@/components/UI/MySelect.vue";
import MyInput from "@/components/UI/MyInput.vue";
import {mapMutations, mapState} from "vuex";
import axios from "axios";

export default {
  components: {MyInput, MyButton, MySelect},
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  data() {
    return {
      complexes: [],
      selectedComplex: -1,

      addressesVisiable: false,
      addresses: [],
      selectedAddress: -1,

      apartmentNumber: '',

      nextStepVisiable: false,
    }
  },
  beforeMount() {

  },
  methods: {
    ...mapMutations({
      setRequestAddressId: "sendRequest/setRequestAddressId",
      setRequestApartmentNumber: "sendRequest/setRequestApartmentNumber"
    }),
    complexChanged(pk) {
      this.selectedComplex = pk
      this.addressesVisiable = true
    },
    addressChanged(pk) {
      this.selectedAddress = pk
      this.nextStepVisiable = true
    },
    async loadComplexes() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/complex/`,
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
    nextStep() {
      this.setRequestAddressId(this.selectedAddress)
      if (this.apartmentNumber !== '') {
        this.setRequestApartmentNumber(this.apartmentNumber)
      }
      this.$emit('nextStep')
    },
  }
}
</script>

<style scoped>
.header-block {
  padding: 10px;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 20px;
}

.step-content-block {
  padding: 10px;
}

.apartment-group {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.apartment-field {
  max-width: 150px;
}

.buttons-block {

}


.container {
  display: flex;
  flex-direction: column;
  //justify-content: space-between;
  min-height: 400px;
  height: 94vh;
  width: 50%;
  border: 1px solid black;
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

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>