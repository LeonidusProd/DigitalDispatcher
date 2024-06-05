<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление ЖК</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Название ЖК</h5>
          <MyInput :placeholder="'Название ЖК'"
                   :model-value="this.complexName"
                   @input="this.complexName = $event.target.value">
          </MyInput>

          <h5>Управляющая компания</h5>
          <MySelect :options="this.offices"
                    @selectChanged="officeChanged">
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
      complexName: '',

      offices: [],
      selectedOffice: -1,
    }
  },
  beforeMount() {
    this.loadOfficees();
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async loadOfficees() {
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
    officeChanged(pk) {
      this.selectedOffice = pk
    },
    async save() {
      if (this.complexName !== '' && this.selectedOffice !== -1) {
        try {
          await axios.post(
              `${this.baseURL}/api/v1/complex/create/`,
              {
                name: this.complexName,
                office: this.selectedOffice
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

        this.complexName = ''
        this.selectedOffice = -1
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