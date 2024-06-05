<template>
  <div class="inside-container"
       v-if="loadOfficesSucsess && loadSchedulesSucsess && loadServicesSucsess">
    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Управляющие компании</h3>
          <SettingsListView :key="this.officesListKey"
                            :empty-header="'Список УК пуст'"
                            :elements-list="this.officesList"
                            :model-name="'office'"
                            @deleteElement="loadOffices">
          </SettingsListView>
        </div>

        <MyButton @click="this.showOfficeDialog = true">
          Добавить УК
        </MyButton>

        <CreateOfficePopup :show="this.showOfficeDialog"
                           @save="saveOffice"
                           @close="this.showOfficeDialog = false">
        </CreateOfficePopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Типовые задачи</h3>
          <SettingsListView :key="this.serviceListKey"
                            :empty-header="'Список типовых задач пуст'"
                            :elements-list="this.servicesList"
                            :model-name="'service'"
                            @deleteElement="loadServices">
          </SettingsListView>
        </div>

        <MyButton @click="this.showServiceDialog = true">
          Добавить типовую задачу
        </MyButton>

        <CreateServicePopup :show="this.showServiceDialog"
                            @save="saveService"
                            @close="this.showServiceDialog = false">
        </CreateServicePopup>
      </div>
    </div>

    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Графики работы</h3>
          <SettingsListView :key="this.scheduleListKey"
                            :empty-header="'Список графиков пуст'"
                            :elements-list="this.schedulesList"
                            :model-name="'schedule'"
                            @deleteElement="loadSchedules">
          </SettingsListView>
        </div>

        <MyButton @click="this.showScheduleDialog = true">
          Добавить график работы
        </MyButton>

        <CreateWorkSchedulePopup :show="this.showScheduleDialog"
                                 @save="saveSchedule"
                                 @close="this.showScheduleDialog = false">
        </CreateWorkSchedulePopup>
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
import SettingsListView from "@/components/Settings/SettingsListView.vue";
import CreateOfficePopup from "@/components/Settings/CreateOfficePopup.vue";
import CreateWorkSchedulePopup from "@/components/Settings/CreateWorkSchedulePopup.vue";
import CreateServicePopup from "@/components/Settings/CreateServicePopup.vue";
import MyButton from "@/components/UI/MyButton.vue";
import {mapState} from "vuex";


export default {
  components: {
    MyButton,
    SettingsListView,
    CreateServicePopup,
    CreateWorkSchedulePopup,
    CreateOfficePopup,
  },
  data() {
    return {
      loadOfficesSucsess: true,
      loadSchedulesSucsess: true,
      loadServicesSucsess: true,
      errorMessage: '',
      errorCode: 0,

      officesList: [],
      officesListKey: 1,
      showOfficeDialog: false,

      schedulesList: [],
      scheduleListKey: 1,
      showScheduleDialog: false,

      servicesList: [],
      serviceListKey: 1,
      showServiceDialog: false,
    }
  },
  beforeMount() {
    this.loadOffices();
    this.loadSchedules();
    this.loadServices();
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
        this.officesList = response.data
      } catch (e) {
        this.errorMessage = `УК: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadOfficesSucsess = false
      }
    },
    saveOffice() {
      this.loadOffices()
      this.officesListKey += 1
      this.showOfficeDialog = false
    },

    async loadSchedules() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/schedule/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.schedulesList = response.data
      } catch (e) {
        this.errorMessage = `Графики работы: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadSchedulesSucsess = false
      }

    },
    saveSchedule() {
      this.loadSchedules();
      this.scheduleListKey += 1
      this.showScheduleDialog = false
    },

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
        this.servicesList = response.data
      } catch (e) {
        this.errorMessage = `Типовые задачи: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadServicesSucsess = false
      }

    },
    saveService() {
      this.loadServices()
      this.servicesList += 1
      this.showServiceDialog = false
    }
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
</style>