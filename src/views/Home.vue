<template>
    <div class="home">
      <h1>OCR Dictaphone App</h1>
      <ImageUploader @image-uploaded="setImage" />
      <TextRecognizer v-if="imageData" :imageData="imageData" @text-recognized="setText" />
      <GoogleVisionOCR v-if="imageData" :imageData="imageData" @text-recognized="setText" />
      <div v-if="recognizedText" class="recognized-text">
        <h2>Texte reconnu :</h2>
        <p>{{ recognizedText }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import ImageUploader from '../components/ImageUploader.vue';
  import TextRecognizer from '../components/TextRecognizer.vue';
  import GoogleVisionOCR from '../components/GoogleVisionOCR.vue';
  
  const imageData = ref(null);
  const recognizedText = ref('');
  
  const setImage = (data) => {
    imageData.value = data;
  };
  
  const setText = (text) => {
    recognizedText.value = text;
  };
  </script>