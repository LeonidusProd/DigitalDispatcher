<template>
  <div class="header-block">
    <h2>Отправить аварийную заявку</h2>

    <h6>На этой странице вы можете отправить аварийную заявку.
      Пощагово мы соберём всю необходимую информацию.</h6>
  </div>

  <MyButton class="next-step-btn"
            @click="$emit('nextStep')">
    <h4>Отправить заявку</h4>
  </MyButton>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";

export default {
  components: {MyButton}
}
</script>

<style scoped>
.header-block {
  padding: 10px;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 20px;
}
.next-step-btn {
  min-width: 60%;
}
</style>