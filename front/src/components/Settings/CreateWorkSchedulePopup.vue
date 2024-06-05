<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление графика работы</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="this.$emit('close')">
          </div>
        </div>

        <div class="down-block">
          <h5>Название графика работы</h5>
          <MyInput :placeholder="'Название графика работы'"
                   :model-value="this.scheduleName"
                   @input="this.scheduleName = $event.target.value">
          </MyInput>

          <h5>Расписание</h5>
          <div class="work-days">
            <div class="work-day">
              <MyCheckbox :checked="mondayIsWork"
                          @update:checked="mondayIsWork = $event"
                          :label="'Понедельник рабочий'"
                          :id=1>
              </MyCheckbox>
              <div class="time-inputs" v-if="mondayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.mondayStartTime"
                         @input="this.mondayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.mondayEndTime"
                         @input="this.mondayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="tuesdayIsWork"
                          @update:checked="tuesdayIsWork = $event"
                          :label="'Вторник рабочий'"
                          :id=2>
              </MyCheckbox>
              <div class="time-inputs" v-if="tuesdayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.tuesdayStartTime"
                         @input="this.tuesdayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.tuesdayEndTime"
                         @input="this.tuesdayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="this.wednesdayIsWork"
                          @update:checked="wednesdayIsWork = $event"
                          :label="'Среда рабочий'"
                          :id=3>
              </MyCheckbox>
              <div class="time-inputs" v-if="this.wednesdayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.wednesdayStartTime"
                         @input="this.wednesdayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.wednesdayEndTime"
                         @input="this.wednesdayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="this.thursdayIsWork"
                          @update:checked="thursdayIsWork = $event"
                          :label="'Четверг рабочий'"
                          :id=4>
              </MyCheckbox>
              <div class="time-inputs" v-if="this.thursdayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.thursdayStartTime"
                         @input="this.thursdayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.thursdayEndTime"
                         @input="this.thursdayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="this.fridayIsWork"
                          @update:checked="fridayIsWork = $event"
                          :label="'Пятница рабочий'"
                          :id=5>
              </MyCheckbox>
              <div class="time-inputs" v-if="this.fridayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.fridayStartTime"
                         @input="this.fridayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.fridayEndTime"
                         @input="this.fridayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="this.saturdayIsWork"
                          @update:checked="saturdayIsWork = $event"
                          :label="'Суббота рабочий'"
                          :id=6>
              </MyCheckbox>
              <div class="time-inputs" v-if="this.saturdayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.saturdayStartTime"
                         @input="this.saturdayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.saturdayEndTime"
                         @input="this.saturdayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
            <div class="work-day">
              <MyCheckbox :checked="this.sundayIsWork"
                          @update:checked="sundayIsWork = $event"
                          :label="'Воскресенье рабочий'"
                          :id=7>
              </MyCheckbox>
              <div class="time-inputs" v-if="this.sundayIsWork">
                <MyInput :placeholder="'С'"
                         :model-value="this.sundayStartTime"
                         @input="this.sundayStartTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
                <p><b>-</b></p>
                <MyInput :placeholder="'До'"
                         :model-value="this.sundayEndTime"
                         @input="this.sundayEndTime = $event.target.value"
                         class="time-input"
                         type="time">
                </MyInput>
              </div>
            </div>
          </div>

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
import MyCheckbox from "@/components/UI/MyCheckBox.vue";
import {mapState} from "vuex";

export default {
  components: {MyCheckbox, MyButton, MySelect, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      scheduleName: '',

      mondayIsWork: false,
      tuesdayIsWork: false,
      wednesdayIsWork: false,
      thursdayIsWork: false,
      fridayIsWork: false,
      saturdayIsWork: false,
      sundayIsWork: false,

      mondayStartTime: '',
      tuesdayStartTime: '',
      wednesdayStartTime: '',
      thursdayStartTime: '',
      fridayStartTime: '',
      saturdayStartTime: '',
      sundayStartTime: '',

      mondayEndTime: '',
      tuesdayEndTime: '',
      wednesdayEndTime: '',
      thursdayEndTime: '',
      fridayEndTime: '',
      saturdayEndTime: '',
      sundayEndTime: '',
    }
  },
  computed: {
    ...mapState({
      baseURL: state => state.main.baseURL,
    })
  },
  methods: {
    async configWorkDays(newSchedulePk, days) {
      try {
        const response = (await axios.get(
            `${this.baseURL}/api/v1/schedule/${newSchedulePk}`,
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))

        let workDays = response.data.work_days

        for (let day in days) {
          await axios.put(
              `${this.baseURL}/api/v1/schedule/workday/manage/${workDays[days[day].dayId - 1].id}`,
              {
                is_not_working: false,
                start_time: days[day].start,
                end_time: days[day].end,
              },
              {
                headers: {
                  'Authorization': `Token ${localStorage.getItem('auth_token')}`
                }
              }
          )
        }
      } catch (e) {
        alert(`Ошибка сохранения\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }
    },
    async save() {
      let days = [];

      if (this.mondayIsWork && this.mondayStartTime !== '' && this.mondayEndTime !== '') {
        days.push({dayId: 1, start: this.mondayStartTime, end: this.mondayEndTime})
      }
      if (this.tuesdayIsWork && this.tuesdayStartTime !== '' && this.tuesdayEndTime !== '') {
        days.push({dayId: 2, start: this.tuesdayStartTime, end: this.tuesdayEndTime})
      }
      if (this.wednesdayIsWork && this.wednesdayStartTime !== '' && this.wednesdayEndTime !== '') {
        days.push({dayId: 3, start: this.wednesdayStartTime, end: this.wednesdayEndTime})
      }
      if (this.thursdayIsWork && this.thursdayStartTime !== '' && this.thursdayEndTime !== '') {
        days.push({dayId: 4, start: this.thursdayStartTime, end: this.thursdayEndTime})
      }
      if (this.fridayIsWork && this.fridayStartTime !== '' && this.fridayEndTime !== '') {
        days.push({dayId: 5, start: this.fridayStartTime, end: this.fridayEndTime})
      }
      if (this.saturdayIsWork && this.saturdayStartTime !== '' && this.saturdayEndTime !== '') {
        days.push({dayId: 6, start: this.saturdayStartTime, end: this.saturdayEndTime})
      }
      if (this.sundayIsWork && this.sundayStartTime !== '' && this.sundayEndTime !== '') {
        days.push({dayId: 7, start: this.sundayStartTime, end: this.sundayEndTime})
      }

      try {
        const response = (await axios.post(
            `${this.baseURL}/api/v1/schedule/create/`,
            {
              name: this.scheduleName,
            },
            {
              headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
              }
            }
        ))
        let newSchedulePk = response.data.id
        await this.configWorkDays(newSchedulePk, days)
      } catch (e) {
        alert(`Ошибка сохранения\n
                Ошибка: ${e.response.status}\n
                Сообщение: ${e.response.data.detail}`)

        this.$emit('close')
      }

      this.$emit('save')

      this.scheduleName = ''
      this.mondayIsWork = false
      this.tuesdayIsWork = false
      this.wednesdayIsWork = false
      this.thursdayIsWork = false
      this.fridayIsWork = false
      this.saturdayIsWork = false
      this.sundayIsWork = false
      this.mondayStartTime = ''
      this.tuesdayStartTime = ''
      this.wednesdayStartTime = ''
      this.thursdayStartTime = ''
      this.fridayStartTime = ''
      this.saturdayStartTime = ''
      this.sundayStartTime = ''
      this.mondayEndTime = ''
      this.tuesdayEndTime = ''
      this.wednesdayEndTime = ''
      this.thursdayEndTime = ''
      this.fridayEndTime = ''
      this.saturdayEndTime = ''
      this.sundayEndTime = ''
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
  min-width: 625px;
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

.work-days {
  display: flex;
  flex-direction: column;
}

.work-day {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 10px;
  min-height: 40px;
}

.time-inputs {
  display: flex;
  flex-direction: row;
}

.time-input {
  width: 100px;
  margin-right: 30px;
  margin-left: 30px;
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