<template>
  <input class="my-input" :value="modelValue" @input="updateInput" :placeholder="this.placeholder">
</template>

<script>
export default {
  name: 'my-input',
  props: {
    modelValue: [String, Number],
    placeholder: [String]
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style scoped>
.my-input{
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212523;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 2px solid #a9a89f;
  border-radius: 10px;
  margin-bottom: 10px;

}
.my-input:focus {
  color: #212523;
  background-color: #fff;
  border-color: #8bb6b1;
  outline: 0;
}
</style>