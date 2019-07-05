#!/bin/bash

timestamp() {
  date +"%Y-%m-%d_%H"
}
msg="/tmp/message.html"

timestamp1(){
date +"%Y-%m-%d"
}
cat $msg | mail -s "$(echo -e " NCC ExtensioCheck scripts updated !!!  $(timestamp1)\nContent-Type: text/html")" -r "success@jenkins141.com" "abhilash@ipsism.co.jp" "gaurav@ipsism.co.jp" "uday@ipsism.co.jp" "vijay@ipsism.co.jp"
