<template>
  <footer class="materials-footer">
    <p>
      © {{ currentYear }} Meichu Hackathon Development Team. All rights
      reserved.
    </p>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      currentYear: new Date().getFullYear(),
    };
  },
};
</script>

<style scoped>
.materials-footer {
  background: #232323;
  text-align: center;
  padding: 20px;
  font-size: 0.9rem;
  color: #aaa;
}
</style>
