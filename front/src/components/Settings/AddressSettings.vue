<template>
  <div class="inside-container"
       v-if="loadAddressesSucsess && loadHousesSucsess && loadComplexesSucsess">
    <div class="outer-block left">
      <div class="inner-block">
        <div>
          <h3>Адреса</h3>

          <SettingsListView :key="this.addressesListKey"
                            :empty-header="'Список адресов пуст'"
                            :elements-list="this.addressesList"
                            :model-name="'address'"
                            @deleteElement="loadAddresses">
          </SettingsListView>
        </div>

        <MyButton @click="this.showAddressDialog = true">
          Добавить адрес
        </MyButton>

        <CreateAddressPopup :show="this.showAddressDialog"
                            @save="saveAddress"
                            @close="this.showAddressDialog = false">
        </CreateAddressPopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Жилой дом</h3>

          <SettingsListView :key="this.housesListKey"
                            :empty-header="'Список жилых домов пуст'"
                            :elements-list="this.housesList"
                            :model-name="'house'"
                            @deleteElement="loadHouses">
          </SettingsListView>
        </div>

        <MyButton @click="this.showHouseDialog = true">
          Добавить жилой дом
        </MyButton>

        <CreateHousePopup :show="this.showHouseDialog"
                          @save="saveHouse"
                          @close="this.showHouseDialog = false">
        </CreateHousePopup>
      </div>
    </div>

    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Жилой комплекс</h3>

          <SettingsListView :key="this.complexesListKey"
                            :empty-header="'Список жилых комплексов пуст'"
                            :elements-list="this.complexesList"
                            :model-name="'complex'"
                            @deleteElement="loadComplexes">
          </SettingsListView>
        </div>

        <MyButton @click="this.showComplexDialog = true">
          Добавить жилой комплекс
        </MyButton>

        <CreateComplexPopup :show="this.showComplexDialog"
                            @save="saveComplex"
                            @close="this.showComplexDialog = false">
        </CreateComplexPopup>
      </div>
    </div>
  </div>
  <div class="alert" v-else>
    <h1>Ошибка загрузки данных, попробуйте ещё раз позже</h1>
    <h4>Ошибка: {{ errorCode }}</h4>
    <h4>Сообщение: {{ errorMessage }}</h4>
  </div>
</template>

<script>
import axios from "axios";
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import SettingsListView from "@/components/Settings/SettingsListView.vue";
import CreateComplexPopup from "@/components/Settings/CreateComplexPopup.vue";
import CreateAddressPopup from "@/components/Settings/CreateAddressPopup.vue";
import CreateHousePopup from "@/components/Settings/CreateHousePopup.vue";
import {mapState} from "vuex";


export default {
  components: {
    CreateAddressPopup,
    CreateComplexPopup,
    CreateHousePopup,
    SettingsListView,
    MyButton,
    MyInput
  },
  data() {
    return {
      loadAddressesSucsess: true,
      loadHousesSucsess: true,
      loadComplexesSucsess: true,
      errorMessage: '',
      errorCode: 0,

      addressesList: [],
      addressesListKey: 1,
      showAddressDialog: false,

      complexesList: [],
      complexesListKey: 1,
      showComplexDialog: false,

      housesList: [],
      housesListKey: 1,
      showHouseDialog: false,
    }
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  beforeMount() {
    this.loadAddresses();
    this.loadComplexes();
    this.loadHouses();
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
        this.addressesList = response.data
      } catch (e) {
        this.errorMessage = `Адреса: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadAddressesSucsess = false
      }
    },
    saveAddress() {
      this.loadAddresses();
      this.addressesListKey += 1
      this.showAddressDialog = false
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
        this.complexesList = response.data
      } catch (e) {
        this.errorMessage = `ЖК: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadComplexesSucsess = false
      }
    },
    saveComplex() {
      this.loadComplexes();
      this.complexesListKey += 1
      this.showComplexDialog = false
    },

    async loadHouses() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/house/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.housesList = response.data
      } catch (e) {
        this.errorMessage = `ЖК: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadHousesSucsess = false
      }
    },
    saveHouse() {
      this.loadHouses();
      this.housesListKey += 1
      this.showHouseDialog = false
    },
  },
}

</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
}

.outer-block {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-right: 20px;
}

.inner-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.left {
  width: 55%;
}
</style>