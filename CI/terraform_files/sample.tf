#begin tf
provider "openstack" {

username:"pnemski"
password:"12345"


}

tasks "mytask" {

apt install vlc



}
