<template>

  <!-- GLOBAL HEADER BEGIN -->
  <header>
    <div class="inner">
      <a class="logo">Blog</a>
      <nav>
        <a href="/">首页</a>
        <a href="/">分类</a>
        <a href="/">归档</a>
      </nav>
      <form class="">
        <input type="text" placeholder="搜索...">
        <button type="submit">
          <icon name="search" scale="1"></icon>
        </button>
      </form>
      <div class="user">
        <icon name="sign-in" scale="1"></icon>
      </div>
    </div>
  </header>
  <!-- GLOBAL HEADER END -->

</template>

<script>
export default {
}
</script>

<style scoped>
@import '../assets/css/header.css';
</style>
