<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-service-content">
        <div class="up-block">
          <h3>Добавление типовой задачи</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Название задачи</h5>
          <MyInput :placeholder="'Название задачи'"
                   :model-value="this.serviceName"
                   @input="this.serviceName = $event.target.value">
          </MyInput>

          <h5>Описание задачи</h5>
          <MyTextarea :placeholder="'Описание задачи'"
                      :model-value="this.serviceDescription"
                      @input="this.serviceDescription = $event.target.value"
                      class="service-description">
          </MyTextarea>

          <h5>Требуемая должность</h5>
          <MySelect :options="this.positions"
                    @selectChanged="positionChanged">
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
import MyTextarea from "@/components/UI/MyTextarea.vue";
import {mapState} from "vuex";

export default {
  components: {MyTextarea, MyButton, MySelect, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      serviceName: '',
      serviceDescription: '',
      positions: [],
      selectedPosition: -1,
    }
  },
  beforeMount() {
    this.loadPositions()
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
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
        this.positions = response.data
      } catch (e) {
        alert(`Должности: Ошибка получения данных\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    positionChanged(pk) {
      this.selectedPosition = pk
    },
    async save() {
      if (this.serviceName !== '' && this.serviceDescription !== '' && this.selectedPosition !== -1) {
        try {
          await axios.post(
              `${this.baseURL}/api/v1/service/create/`,
              {
                name: this.serviceName,
                description: this.serviceDescription,
                position: this.selectedPosition
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
        this.serviceName = ''
        this.serviceDescription = ''
        this.selectedPosition = -1
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
  min-width: 600px;
  padding: 20px;
  display: flex;
}

.create-service-content {
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

.service-description {
  height: 150px;
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