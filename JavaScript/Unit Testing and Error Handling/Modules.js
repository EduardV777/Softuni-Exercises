let admin = "Eduard", password = "123456";

function ReturnPermissionDenied() {
    return console.error("Permission Denied!");
}

function ReturnSuccessfulConnection() {
    return console.log('Connected!');
}


function EstablishConnection(adminName, adminPass) {

    if(adminName != admin){
        return ReturnPermissionDenied();
    }
    if(password != password){
        return ReturnPermissionDenied();
    }

    return ReturnSuccessfulConnection();
}


module.exports = EstablishConnection;