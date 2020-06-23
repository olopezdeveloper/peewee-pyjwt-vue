new Vue({
  el: '#starting',
  delimiters: ['${','}'],
  data: {
    login: { 
      username: '',
      password: ''
    },
    loading: true,
  },
  mounted: function() {
     this.loading = false;
  },
  methods: {
      doLogin: function() {
        this.loading = true;
        const res = fetch(`/ajax-service/`, {
        method: 'POST',
        body: JSON.stringify({
            url: 'login/',
            username: this.login.username,
            password: this.login.password
          })
        }).then((response) =>{
          this.loading = false;
          response.json().then(function(data){
              if (data['status_code']==200) {
                localStorage.setItem('token', data['token']);
                window.location.href = '/notes/';
              }else{
                alert("Usuario o Contraseña incorrecto, intenta de nuevo!");
              }
          });
        }).catch(err => {
          this.loading = false;
          console.log("Error!")
          console.log(err)
        });
      
      } 
    }
  });
