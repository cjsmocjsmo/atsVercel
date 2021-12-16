<script>
  let name = '';
  let message = '';
</script>

<!-- <h1>Comments</h1> -->

<form action="“”" method="“post”">
  <input type="“text”" name="“name”" value="Name" /> <br />
  <input type="“text”" name="“email”" value="Email" /> <br />
  <input type="“text”" name="“address”" value="Address(optional)" /><br />
  <h3>Leave A Comment:</h3>
  <br /><textarea name="“message”" rows="“25”" cols="“120”" /><br />
  <input class="foo" type="submit" value="Post Comment" />
</form>

<style>
    .foo {
        font-size: 1.5em;
    }

    input {
        width: 100%;
        height: 2em;
        background-color: grey;
        color: whitesmoke;
        border-radius: 7px;
        margin: 7px;
    }

    textarea {
        width: 100%;
        height: 20em;
        border-radius: 10px;
    }
</style>
