<template>
<!--  <input class="my-textfield" :value="modelValue" @input="updateInput" :placeholder="this.placeholder" type="text">-->
  <textarea class="my-textarea custom-scroll" :value="modelValue" @input="updateInput" :placeholder="this.placeholder" ></textarea>
</template>

<script>
export default {
  name: 'my-textarea',
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
.my-textarea {
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
  resize: none;
}
.my-textarea:focus {
  color: #212523;
  background-color: #fff;
  border-color: #8bb6b1;
  outline: 0;
}
.custom-scroll::-webkit-scrollbar {
  width: 5px;
}
.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
  border-radius: 6px;
}
.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>