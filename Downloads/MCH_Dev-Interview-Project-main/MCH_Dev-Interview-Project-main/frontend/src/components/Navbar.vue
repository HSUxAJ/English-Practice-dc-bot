<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <img src="/images/mch.webp" alt="Logo" class="logo" />
      <router-link to="/" class="brand-link">梅竹黑客松 開發部面試專案</router-link>
    </div>
    <ul class="navbar-nav">
      <li class="nav-item">
        <router-link to="/" class="nav-link">自我介紹</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/historical-websites" class="nav-link"
          >歷年網站</router-link
        >
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.navbar {
  display: flex;
  align-items: center;
  background-color: #232323;
  padding: 1rem 5rem;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.navbar-brand {
  display: flex;
  align-items: center;
  flex-grow: 1;
}

.logo {
  height: 24px;
  width: 24px;
  margin-right: 10px;
}

.brand-link {
  color: #fff;
  font-size: 1.25rem;
  font-weight: bold;
  text-decoration: none;
}

.navbar-nav {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-item {
}

.nav-link {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #ddd;
}
</style>
