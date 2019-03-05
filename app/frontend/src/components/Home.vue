<template>
  <div class="pusher">
    <div class="ui vertical masthead center aligned segment">
      <div class="ui container">
      </div>
      <div class="ui text container">
        <h1 class="ui header">
          <img src="../assets/logo.png">
        </h1>
        <h2>Get tweets by twitter handle</h2>
        <form method="get" @submit.prevent="checkForm">
          <div v-if="errors.length">
            <ul>
              <div class="ui visible red message" v-for="error in errors">
                <p>{{ error }}</p>
              </div>
            </ul>
          </div>
          <div class="ui big icon input" v-bind:class="{ loading: isLoading}">
            <input type="text" placeholder="Enter a twitter handle" v-model="keyword">
            <i class="search icon"></i>
          </div>
          <button class="ui huge primary button">Submit <i class="right arrow icon"></i></button>
        </form>

        <div class="results">
          <h3 class="results-header" v-if="keyword != null && errors.length == 0 && isLoading == false">
            Result for twitter handle {{ this.keyword }}:</h3>
          <div class="ui feed">
            <div class="event" v-for="tweet in tweets">
              <div class="label">
                <img v-bind:src="tweet.user.profile_image_url">
              </div>
              <div class="content">
                <div class="date">
                  {{ tweet.created_at }}
                </div>
                <div class="summary">
                   {{ tweet.text }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import './Home.css'

  export default {
    data() {
      return {
        errors: [],
        keyword: null,
        tweets: [],
        isLoading: false,
      }
    },
    methods: {
      getTweets() {
        this.tweets = this.getTweetsFromBackend()
      },
      getTweetsFromBackend() {
        const keyword = this.keyword;
        const path = `${process.env.API_URL}/tweets/?user=${keyword}&count=3`;
        let self = this;
        axios.get(path)
          .then(response => {
            this.tweets = response.data
          })
          .catch(error => {
            this.errors.push(error);
          })
          .then(function () {
            self.isLoading = false;
          });
      },
      checkForm() {
        this.errors = [];
        this.isLoading = true;
        if (this.keyword) {
          this.getTweets();
          return true;
        }

        this.errors = [];
        this.tweets = [];

        if (!this.keyword) {
          this.errors.push('Twitter handle is required.');
        }
        this.isLoading = false;
      },
    },
    created() {
    }
  }
</script>
