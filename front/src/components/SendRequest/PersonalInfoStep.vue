<template>
  <div class="container">
    Ввод персональных
<!--    <h5>Выберите свой жилой комплекс</h5>-->
<!--    <MySelect>-->

<!--    </MySelect>-->

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
import MySelect from "@/components/UI/MySelect.vue";

export default {
  components: {MySelect}
  // components: {OrganizationSettings, StaffSettings, AddressSettings, SystemSettings, MyButton},
  // computed: {
  //   ...mapState({
  //     baseURL: state => state.main.baseURL,
  //   })
  // },
  // data() {
  //   return {
  //     activeSection: 'systemSettings',
  //   }
  // },
  // methods: {
  //   async loguot() {
  //     try {
  //       await axios.post(
  //           `${this.baseURL}/auth/token/logout`,
  //           {},
  //           {
  //             headers: {
  //               'Authorization': `Token ${localStorage.getItem('auth_token')}`
  //             }
  //           }
  //       )
  //       localStorage.removeItem('auth_token');
  //       localStorage.removeItem('user_role');
  //
  //       this.$router.push('/');
  //     } catch (e) {
  //       alert(`Ошибка выхода\n
  //               Ошибка: ${e.response.status}\n
  //               Сообщение: ${e.response.data.detail}`)
  //     }
  //   }
  // }
}
</script>

<style scoped>
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