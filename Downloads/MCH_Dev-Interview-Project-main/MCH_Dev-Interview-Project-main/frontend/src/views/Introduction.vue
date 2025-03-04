<template>
  <div class="introduction">
    <header class="intro-header">
      <img src="/src/assets/pic.jpg" alt="pic" class="profile-pic" />
      <div class="intro-text">
        <h2>徐滙傑</h2>
        <p>清大工業工程與工程管理系大二，有多次開發 LINE Bot 的經驗，但對網頁的開發(css癌)以及團隊製作專案並沒有甚麼經驗，希望可以加入這個大家庭學習😆</p>
      </div>
    </header>
    <section class="about-section">
      <div class="info-card">
        <h3>🏆 得獎紀錄</h3>
        <ul>
          <li>113 學年度上學期書卷獎</li>
          <li>110 學年度臺北市資訊能力競賽 佳作</li>
          <li>111 學年度中正高中資訊科能力競賽 第二名</li>
          <li>110 學年度中正高中資訊科能力競賽 佳作</li>
          <li>2023 年第八屆 YTP 少年圖靈計畫 決賽</li>
          <li>2022 年第七屆 YTP 少年圖靈計畫 決賽</li>
          <li>2022 年全國高級中學第14屆生活科技學藝競賽 優等</li>
          <li>APCS 觀念、實作 4+4</li>
          <li>2023 Math Kangaroo Taiwan 袋鼠數學比賽 銀牌獎</li>
          <li>2022 TOI 新手同好會 個人賽 15名</li>
          <a></a>
        </ul>
      </div>

      <div class="info-card">
        <h3>💡 製作過的小專案主題(點擊名稱看細節)</h3>
        <ul>
          <li v-for="(item, index) in projects" :key="index" @click="showDetails(item)">
            {{ item.name }}
          </li>
        </ul>

        <div v-if="showDetailModal" class="detail-modal">
          <div class="modal-content">
            <h4>{{ selectedProject.name }}</h4>
            <p>{{ selectedProject.details }}</p>
            <a :href="selectedProject.link" target="_blank" class="project-link">查看專案</a>
            <button @click="closeModal">關閉</button>
          </div>
        </div>
      </div>

      <div class="info-card">
        <h3>💻 熟練語言</h3>
        <ul>
          <li>C</li>
          <li>C++</li>
          <li>Python</li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDetailModal: false,
      selectedProject: {},
      projects: [
        { 
          name: "Line_bot_manager (python)", 
          details: "利用LineBotApi製作出能夠分析excel所提供的指示，在規定的時間傳訊息給駕駛，若駕駛沒有在規定的時間內回覆，則回報管理者。",
          link: "https://github.com/HSUxAJ/Line_bot_manager" 
        },
        { 
          name: "English-Practice-dc-bot (python)", 
          details: "使用爬蟲分析Quizlet單字集與劍橋英語辭典，將辭典中單字集上的單字例句挖空，製作成多個填空題，讓Discord Chat Bot輸出，使用戶透過解題學習生字。",
          link: "https://github.com/HSUxAJ/English-Practice-dc-bot" 
        },
        { 
          name: "Line-Discord (python)", 
          details: "實現Discord與Line雙向串接，透過串接兩邊Chat Bot Api，能夠同時在兩端發送與接收訊息，實現訊息管理。Ex.能夠Discord能收發line的訊息。",
          link: "https://github.com/HSUxAJ/Line-Discord-v2" 
        },
        
        { 
          name: "SMTP (python)", 
          details: "利用PyQt5製作視窗與使用者互動，能夠在上面上傳excel及確認發送email。",
          link: "https://github.com/HSUxAJ/SMTP" 
        },
        { 
          name: "Excel_analyze (python)", 
          details: "利用PyQt5製作視窗與使用者互動，能夠在上面上傳excel及下載優化過後的excel。",
          link: "https://github.com/HSUxAJ/Excel_analyze" 
        },
        { 
          name: "SayMore (Vue)", 
          details: "自製的旅遊網站，當中功能包含與firebase資料庫的連結、行程區、行程細節介紹、貼文功能、登入系統等。",
          link: "https://github.com/HSUxAJ/SayMore" 
        },
      ]
    };
  },
  methods: {
    showDetails(project) {
      this.selectedProject = project; 
      this.showDetailModal = true;
    },
    closeModal() {
      this.showDetailModal = false;
    }
  }
};
</script>

<style scoped>
.introduction {
  padding: 40px 20px;
  max-width: 900px;
  margin: 0 auto;
}

.intro-header {
  background-color: #f8f9fa;
  padding: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
}

.profile-pic {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-left: 30px;
  
  border: 4px solid #ffffff;
  outline: 5px solid rgb(22, 180, 43);
}


.intro-text {
  display: flex;
  flex-direction: column;
  line-height: 1.5;
}

.intro-text h2 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #000000;
}

.intro-text p {
  font-size: 1.1rem;
  color: #333;
}

/* 區塊設計 */
.about-section {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.info-card {
  background: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.info-card:hover {
  transform: translateY(-5px);
}

.info-card h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #333;
}
.detail-modal {
  margin-top: 20px; 
  background-color: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
.modal-content {
  padding: 20px;
}

.modal-content h4 {
  font-size: 1.8rem;
  margin-bottom: 15px;
  color: #333;
  font-weight: bold;
}

.modal-content p {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

.modal-content .project-link {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border-radius: 8px;
  
  text-decoration: none;
  margin-bottom: 15px;
}

.modal-content .project-link:hover {
  background-color: #0056b3;
}

.modal-content button {
  padding: 10px 20px ;
  background-color: #656d73;
  color: white;
  border-radius: 8px;
  border: none;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.modal-content button:hover {
  background-color: #4b5457;
}

.about-section ul {
  list-style-type: disc;
  padding-left: 20px;
}

.about-section li {
  font-size: 1rem;
  line-height: 1.8;
  color: #444;
  padding-left: 5px;
  transition: color 0.3s;
}
</style>
