import 'package:flutter/material.dart';

class MainScreen extends StatelessWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Welcome"),
        backgroundColor: Color.fromRGBO(230, 203, 199, 0.5),
      ),
      body: Center(
        child: Column(
          children: [
            Image.asset(
              "assets/images/welcome.png",
              width: 600,
            ),
            Text(
              "Janaki Vinod",
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(
              height: 16,
            ),
            Text(
              "I am Janaki Vinod, a fresher studying at Amrita School of Engineering, Amritapuri",
              style: TextStyle(fontSize: 18),
            )
          ],
        ),
      ),
    );
  }
}
