  Vue.http.headers.common['token'] = "{{ csrf_token }}";
  new Vue({
    el: '#starting',
    delimiters: ['${','}'],
    data: {
      notes: [],
      newNote: { 'text': null}, 
      loading: true,
    },
    mounted: function() {
      if (typeof localStorage['token'] === 'undefined')
        this.logout();
      this.getNotes();
    },
    methods: {
      getNotes: function() {
        this.loading = true;

        const res = fetch(`/ajax-service/`, {
        method: 'POST',
        body: JSON.stringify({
            url: 'notes/',
            token: localStorage['token'],
            use_method: 'get'
          })
        }).then((response)=> {
          this.loading = false;
          response.json().then((data)=>{
              console.log(data);
              if (data['status_code']==200) {
                this.notes = data['results']
              }else{
                // Log Server
                alert("Algo esta mal, favor recarga la pagina!");
              }              
          });
        }).catch(err => {
          this.loading = false;
          console.log("Error!")
          console.log(err)
        });
      },
      logout: function() {
        localStorage.removeItem('token');
        window.location.href = '/';
      },
      addNote: function() {
        this.loading = true;

        const res = fetch(`/ajax-service/`, {
        method: 'POST',
        body: JSON.stringify({
            url: 'notes/',
            token: localStorage['token'],
            text: this.newNote['text']
          })
        }).then((response) => {
          this.loading = false;
          response.json().then((data)=>{
              console.log(data);
              if (data['status_code']==201) {
                this.getNotes();
                $('#addNoteModal').modal('toggle');
                this.newNote['text'] = ''; //Limpiamos el campo texto
              }else{
                // Log Server
                alert(`Algo esta mal, ${data["text"]}!`);
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