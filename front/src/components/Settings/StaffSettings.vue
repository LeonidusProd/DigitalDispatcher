<template>
  <div class="inside-container"
       v-if="loadDepartmentsSucsess && loadPositionsSucsess && loadEmployeesSucsess">
    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Отделы</h3>

          <SettingsListView :key="this.departmentsListKey"
                            :empty-header="'Список отделов пуст'"
                            :elements-list="this.departmentsList"
                            :model-name="'department'"
                            @deleteElement="loadDepartments">
          </SettingsListView>
        </div>

        <MyButton @click="this.showDepartmentDialog = true">
          Добавить отдел
        </MyButton>

        <CreateDepartmentPopup :key="this.departmentsPopupKey"
                               :show="this.showDepartmentDialog"
                               @save="saveDepartment"
                               @close="this.showDepartmentDialog = false">
        </CreateDepartmentPopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Должности</h3>

          <SettingsListView :key="this.positionsListKey"
                            :empty-header="'Список должностей пуст'"
                            :elements-list="this.positionsList"
                            :model-name="'position'"
                            @deleteElement="loadPositions">
          </SettingsListView>
        </div>

        <MyButton @click="this.showPositionDialog = true">
          Добавить должность
        </MyButton>

        <CreatePositionPopup :key="this.positionsPopupKey"
                             :show="this.showPositionDialog"
                             @save="savePosition"
                             @close="this.showPositionDialog = false">
        </CreatePositionPopup>
      </div>
    </div>

    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Сотрудники</h3>

          <SettingsListView :key="this.employeesListKey"
                            :empty-header="'Список сотрудников пуст'"
                            :elements-list="this.employeesList"
                            :model-name="'employee'"
                            @deleteElement="loadEmployees">
          </SettingsListView>
        </div>

        <MyButton @click="this.showEmployeeDialog = true">
          Добавить сотрудника
        </MyButton>

        <CreateEmployeePopup :key="this.employeesPopupKey"
                             :show="this.showEmployeeDialog"
                             @save="saveEmployee"
                             @close="this.showEmployeeDialog = false">
        </CreateEmployeePopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Пользователи</h3>

          <SettingsListView :key="this.usersListKey"
                            :empty-header="'Список пользователей пуст'"
                            :elements-list="this.usersList"
                            :model-name="'user'"
                            @deleteElement="loadUsers">
          </SettingsListView>
        </div>

        <MyButton @click="this.showUserDialog = true">
          Добавить пользователя
        </MyButton>

        <CreateUserPopup :key="this.usersPopupKey"
                             :show="this.showUserDialog"
                             @save="saveUser"
                             @close="this.showUserDialog = false">
        </CreateUserPopup>
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
import CreateDepartmentPopup from "@/components/Settings/CreateDepartmentPopup.vue";
import CreatePositionPopup from "@/components/Settings/CreatePositionPopup.vue";
import CreateEmployeePopup from "@/components/Settings/CreateEmployeePopup.vue";
import {mapState} from "vuex";
import CreateUserPopup from "@/components/Settings/CreateUserPopup.vue";


export default {
  components: {
    CreateUserPopup,
    CreateEmployeePopup,
    CreatePositionPopup,
    CreateDepartmentPopup,
    SettingsListView,
    MyButton,
    MyInput
  },
  data() {
    return {
      loadDepartmentsSucsess: true,
      loadPositionsSucsess: true,
      loadEmployeesSucsess: true,
      loadUsersSucsess: true,
      errorMessage: '',
      errorCode: 0,

      departmentsList: [],
      departmentsListKey: 1,
      departmentsPopupKey: 1,
      showDepartmentDialog: false,

      positionsList: [],
      positionsListKey: 1,
      positionsPopupKey: 1,
      showPositionDialog: false,

      employeesList: [],
      employeesListKey: 1,
      employeesPopupKey: 1,
      showEmployeeDialog: false,

      usersList: [],
      usersListKey: 1,
      usersPopupKey: 1,
      showUserDialog: false,
    }
  },
  beforeMount() {
    this.loadDepartments();
    this.loadPositions();
    this.loadEmployees();
    this.loadUsers();
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async loadDepartments() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/department/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.departmentsList = response.data
      } catch (e) {
        this.errorMessage = `Отделы: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadDepartmentsSucsess = false
      }
      this.positionsListKey += 1
    },
    saveDepartment() {
      this.loadDepartments()
      this.positionsPopupKey += 1
      this.departmentsListKey += 1
      this.showDepartmentDialog = false
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
        this.positionsList = response.data
      } catch (e) {
        this.errorMessage = `Должности: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadPositionsSucsess = false
      }
      this.employeesListKey += 1
    },
    savePosition() {
      this.loadPositions()
      this.employeesPopupKey += 1
      this.positionsListKey += 1
      this.showPositionDialog = false
    },

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
        this.employeesList = response.data
      } catch (e) {
        this.errorMessage = `УК: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadEmployeesSucsess = false
      }
    },
    saveEmployee() {
      this.loadEmployees()
      this.employeesListKey += 1
      this.showEmployeeDialog = false
    },

    async loadUsers() {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/user/`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        this.usersList = response.data
      } catch (e) {
        this.errorMessage = `УК: ${e.response.data.detail}`
        this.errorCode = e.response.status

        this.loadUsersSucsess = false
      }
    },
    saveUser() {
      this.loadUsers()
      this.usersListKey += 1
      this.showUserDialog = false
    }
  }
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