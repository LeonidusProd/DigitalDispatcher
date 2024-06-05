<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление должности</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Название должности</h5>
          <MyInput :placeholder="'Название должности'"
                   :model-value="this.positionName"
                   @input="this.positionName = $event.target.value">
          </MyInput>

          <h5>Отдел</h5>
          <MySelect :options="this.departments"
                    @selectChanged="departmentChanged">
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
      positionName: '',
      selectedDepartment: -1,
      departments: [],
    }
  },
  beforeMount() {
    this.loadDepartments()
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
        this.departments = response.data
      } catch (e) {
        alert(`Отделы: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    departmentChanged(pk) {
      this.selectedDepartment = pk
    },
    async save() {
      if (this.positionName !== '' && this.selectedDepartment !== -1) {
        try {
          await axios.post(
              `${this.baseURL}/api/v1/position/create/`,
              {
                name: this.positionName,
                department: this.selectedDepartment
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
        this.positionName = ''
        this.selectedDepartment = -1
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