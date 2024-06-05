<template>
  <div class="container">
    <div class="left-side-menu">
      <div class="up-block">
        <div class="logo-block">
          <img class="logo-img" src="@/assets/Лого%20текст%20снизу.svg" alt="logo">
        </div>
        <div class="menu-block">
          <MyButton @click="this.activeSection = 'systemSettings'"
                    :class="{'active-button':this.activeSection === 'systemSettings'}">
            Системные
          </MyButton>
          <MyButton @click="this.activeSection = 'organizationSettings'"
                    :class="{'active-button':this.activeSection === 'organizationSettings'}">
            Организация
          </MyButton>
          <MyButton @click="this.activeSection = 'staffSettings'"
                    :class="{'active-button':this.activeSection === 'staffSettings'}">
            Персонал
          </MyButton>
          <MyButton @click="this.activeSection = 'addressSettings'"
                    :class="{'active-button':this.activeSection === 'addressSettings'}">
            Адреса
          </MyButton>
        </div>
      </div>
      <div class="down-block">
        <MyButton @click="this.$router.push('/requests')">
          Управление заявками
        </MyButton>
        <MyButton @click="loguot">
          Выход
        </MyButton>
      </div>
    </div>

    <div class="workspace">
      <SystemSettings v-if="this.activeSection === 'systemSettings'">
      </SystemSettings>

      <OrganizationSettings v-if="this.activeSection === 'organizationSettings'">
      </OrganizationSettings>

      <StaffSettings v-if="this.activeSection === 'staffSettings'">
      </StaffSettings>

      <AddressSettings v-if="this.activeSection === 'addressSettings'">
      </AddressSettings>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import {mapState} from "vuex";
import SystemSettings from "@/components/Settings/SystemSettings.vue";
import AddressSettings from "@/components/Settings/AddressSettings.vue";
import StaffSettings from "@/components/Settings/StaffSettings.vue";
import OrganizationSettings from "@/components/Settings/OrganizationSettings.vue";
import axios from "axios";

export default {
  components: {OrganizationSettings, StaffSettings, AddressSettings, SystemSettings, MyButton},
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  data() {
    return {
      activeSection: 'systemSettings',
    }
  },
  methods: {
    async loguot() {
      try {
        await axios.post(
            `${this.baseURL}/auth/token/logout`,
            {},
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        )
        localStorage.removeItem('auth_token');
        localStorage.removeItem('user_role');

        this.$router.push('/');
      } catch (e) {
        alert(`Ошибка выхода\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)
      }
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  min-height: 400px;
  height: 94vh;
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