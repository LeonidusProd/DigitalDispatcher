<template>
  <div class="container">

    <StartStep v-if="activeStep === 'start'"
               @nextStep="activeStep = 'address'">
    </StartStep>

    <AddressStep v-if="activeStep === 'address'"
                 @nextStep="activeStep = 'body'">
    </AddressStep>

    <RequestBodyStep v-if="activeStep === 'body'"
                     @nextStep="activeStep = 'person'"
                     @previousStep="activeStep = 'address'">
    </RequestBodyStep>

    <PersonalInfoStep v-if="activeStep === 'person'"
                      @previousStep="activeStep = 'body'"
                      @sandRequest="">
    </PersonalInfoStep>

    <!--    <div class="buttons-block">-->
    <!--      <MyButton class="previous-step"-->
    <!--                @click="previous_step"-->
    <!--                v-if="activeStep !== 'start'">-->
    <!--        <h4>Назад</h4>-->
    <!--      </MyButton>-->

    <!--      <MyButton class="next-step-or-save"-->
    <!--                @click="next_step"-->
    <!--                v-if="activeStep !== 'person'">-->
    <!--        <h4>Следующий шаг</h4>-->
    <!--      </MyButton>-->

    <!--      <MyButton class="next-step-or-save"-->
    <!--                @click="next_step"-->
    <!--                v-if="activeStep === 'person'">-->
    <!--        <h4>Отправить заявку</h4>-->
    <!--      </MyButton>-->
    <!--    </div>-->

  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MySelect from "@/components/UI/MySelect.vue";
import AddressStep from "@/components/SendRequest/AddressStep.vue";
import RequestBodyStep from "@/components/SendRequest/RequestBodyStep.vue";
import PersonalInfoStep from "@/components/SendRequest/PersonalInfoStep.vue";
import StartStep from "@/components/SendRequest/StartStep.vue";

export default {
  components: {StartStep, MyButton, PersonalInfoStep, RequestBodyStep, AddressStep, MySelect},
  // computed: {
  //   ...mapState({
  //     baseURL: state => state.main.baseURL,
  //   })
  // },
  data() {
    return {
      activeStep: 'start',
    }
  },
  methods: {
    previous_step() {
      if (this.activeStep === 'person') {
        this.activeStep = 'body'
      } else if (this.activeStep === 'body') {
        this.activeStep = 'address'
      } else if (this.activeStep === 'address') {
        this.activeStep = 'start'
      }
    },
    next_step() {
      if (this.activeStep === 'start') {
        this.activeStep = 'address'
      } else if (this.activeStep === 'address') {
        this.activeStep = 'body'
      } else if (this.activeStep === 'body') {
        this.activeStep = 'person'
      }
    },


  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  min-height: 400px;
  height: 94vh;
  width: 50%;
  border: 1px solid black;
  background-color: rgb(169, 168, 159, 0.2);
  border-radius: 20px;
  padding: 20px;
}

.buttons-block {
  display: flex;
  flex-direction: row;
  width: 100%;
  gap: 20px;
  justify-content: center;
  border: 1px solid blue;
}

.previous-step {
  min-width: 20%;
}

.next-step-or-save {
  min-width: 60%;
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