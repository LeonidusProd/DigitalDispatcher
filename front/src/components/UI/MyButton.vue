<template>
<!--  <button class="my-btn my-btn-primary">-->
<!--    <slot></slot>-->
<!--  </button>-->
  <div class="my-button">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'my-button',
}
</script>

<style scoped>
.my-button {
  display: flex;
  flex-direction: column;
  //width: 150px;
  background-color: rgb(139, 182, 177, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  justify-content: space-evenly;
  text-align: center;
}

.my-button:hover {
  display: flex;
  flex-direction: column;
  //width: 150px;
  background-color: rgb(109, 197, 195, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  justify-content: space-evenly;
  text-align: center;
  cursor: default;
}

.my-btn {
  margin-top: 5px;
  text-decoration: none;
  --bs-btn-padding-x: 0.75rem;
  --bs-btn-padding-y: 0.375rem;
  display: inline-block;
  padding: var(--bs-btn-padding-y) var(--bs-btn-padding-x);
  font-size: 1rem;
  color: #212523;
  background-color: #4fd4d5;
  text-align: center;
  vertical-align: middle;
  border: var(--bs-btn-border-width) solid var(--bs-btn-border-color);
  border-radius: 7px;
}

.my-btn:focus {
  background-color: #6dc5c3;
  border-color: #122b40
}
</style>