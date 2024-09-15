<template>
    <div class="image-uploader">
      <FileUpload mode="basic" name="image" :customUpload="true" @uploader="onUpload" accept="image/*" :auto="true" />
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import FileUpload from 'primevue/fileupload'
  
  export default defineComponent({
    name: 'ImageUploader',
    components: { FileUpload },
    emits: ['image-uploaded'],
    setup(props, { emit }) {
      const onUpload = (event) => {
        const file = event.files[0]
        const reader = new FileReader()
        reader.onload = (e) => {
          emit('image-uploaded', e.target.result)
        }
        reader.readAsDataURL(file)
      }
  
      return { onUpload }
    }
  })
  </script>