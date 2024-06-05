<template>
  <input type="checkbox"
         class="my-checkbox"
         :checked="checked"
         @change="updateCheckbox"
         :id="id">
  <label :for="id">{{ this.label }}</label>
</template>

<script>
export default {
  name: 'my-checkbox',
  props: {
    id: [Number],
    checked: [Boolean],
    label: [String]
  },
  methods: {
    updateCheckbox(event) {
      console.log(this.label + ' Checkbox clicked: ' + event.target.checked)
      this.$emit('update:checked', event.target.checked)
    }
  }
}
</script>

<style scoped>
.my-checkbox {
  position: absolute;
  z-index: -1;
  opacity: 0;
}
.my-checkbox + label {
  display: inline-flex;
  align-items: center;
  user-select: none;
}
.my-checkbox + label::before {
  content: '';
  display: inline-block;
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  flex-grow: 0;
  border: 1px solid #a9a89f;
  border-radius: 0.25em;
  margin-right: 0.5em;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: 50% 50%;
}
.my-checkbox:checked + label::before {
  border-color: rgb(79, 212, 213);
  background-color: rgb(79, 212, 213);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e");
}
.my-checkbox:not(:disabled):not(:checked) + label:hover::before {
  border-color: #b3d7ff;
}
.my-checkbox:not(:disabled):active + label::before {
  background-color: rgb(79, 212, 213, 0.5);
  border-color: rgb(79, 212, 213, 0.5);
}
.my-checkbox:disabled + label::before {
  background-color: #e9ecef;
}
</style>