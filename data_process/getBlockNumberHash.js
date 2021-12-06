//BS-DREAM is a Distributed Reliability Evaluation and Analysis Mechanism for Block Services

var http = require('http');
var fs = require('fs');
var web3 = require('web3');
web3.setProvider(new web3.providers.HttpProvider("https://mainnet.infura.io"));

var fsread = fs.readFileSync("blocknumber.txt").toString().split("\n")

var blocknumber=[]

for (i in fsread)
	blocknumber.push(fsread[i].split(",")[1])

var hehe=44800;
var hehe2=blocknumber.length;
var yici = 100;
var getshu = 0

function getone(number) {
	--getshu;
	web3.eth.getBlock(number, function(err, data){
		if (!err) {
			if (data!=null && data.number!=null)
				fs.appendFileSync("BlockNumerHash.csv", data.number+","+data.hash+"\n");
			else
				console.log(number);
		}
		else{
			console.log(err, data);
			getone(number);
		}

		++getshu;
		if(getshu==0) {
			hehe+=yici;
			huoquyipi();
		}
	});
}

function huoquyipi() {
	var qidian = hehe;
	var mubiao = hehe+100;
	if (mubiao>hehe2)
		mubiao = hehe2;

	console.log(Date(Date.now()).substr(16,9), qidian, mubiao);
	for (var i = qidian; i<mubiao;++i) {
		getone(parseInt(blocknumber[i]));
	}
}

huoquyipi();