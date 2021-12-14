<script>

let name = '';
let message = "";

</script>

<h1>Leave A Comment</h1>

<form action=“” method=“post”>
    <input type=“text” name=“name” value="Name"> <br />
    <input type=“text” name=“email” value="Email"> <br />
    <input type=“text” name=“address” value="Address(optional)"/><br />
    <h3>Message:</h3> <br /><textarea name=“message” rows=“25” cols=“120”></textarea><br />
    <input type="submit" value="Submit">
</form>

<style>

    input {
        width: 100%;
        height: 2em;
        background-color: grey;
        color: whitesmoke;
        border-radius: 10px;
    }

    textarea {
        width: 100%;
        height: 20em;
        border-radius: 10px;
    }


</style>