import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:flutter_introduction/screens/main_screen.dart';
import 'package:introduction_screen/introduction_screen.dart';

class OnboardingScreen extends StatefulWidget {
  @override
  _OnboardingScreenState createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  final introKey = GlobalKey<IntroductionScreenState>();

  void _onIntroEnd(context) {
    Navigator.push(
        context, MaterialPageRoute(builder: (context) => MainScreen()));
  }

  Widget _buildImage(String assetName, [double width = 350]) {
    return Padding(
      padding: const EdgeInsets.only(
        top: 50,
      ),
      child: Image.asset(
        'assets/$assetName',
        width: width,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    const bodyStyle = TextStyle(fontSize: 19.0);

    const pageDecoration = const PageDecoration(
      titleTextStyle: TextStyle(fontSize: 28.0, fontWeight: FontWeight.w700),
      bodyTextStyle: bodyStyle,
      descriptionPadding: EdgeInsets.fromLTRB(16.0, 0.0, 16.0, 16.0),
      pageColor: Color(0xFAFAFA),
      imagePadding: EdgeInsets.zero,
    );

    return IntroductionScreen(
      key: introKey,
      globalBackgroundColor: Color.fromRGBO(215, 203, 199, 1),

      pages: [
        PageViewModel(
            title: "YOGA SURGE",
            //body:
            //    "Welcome to the Yoga world \n\nInhale the future, exhale the past",
            image: _buildImage('images/page1.png'),
            decoration: pageDecoration,
            bodyWidget: Column(
              children: [
                Text(
                  "Welcome to the Yoga world",
                  style: TextStyle(fontSize: 24),
                ),
                SizedBox(
                  height: 32,
                ),
                Text("Inhale the future, exhale the past",
                    style: TextStyle(fontSize: 16)),
              ],
            )),
        PageViewModel(
          title: "Healthy Freaks exercises",
          body: "Letting go is the hardest asana",
          image: _buildImage(
            'images/page2.png',
          ),
          decoration: pageDecoration,
        ),
        PageViewModel(
          title: "Cycling",
          body:
              "You cannot always control what goes on outside. But you can always control what goes on inside",
          image: _buildImage('images/page3.png'),
          decoration: pageDecoration,
        ),
        PageViewModel(
          title: "Meditation",
          body: "The longest journey of any person is the journey inward",
          image: _buildImage('images/page4.png', 320),
          /* footer: ElevatedButton(
            onPressed: () {
              introKey.currentState?.animateScroll(0);
            },
            child: Text(
              "Start over",
              style: TextStyle(color: Colors.white),
            ),
            style: ElevatedButton.styleFrom(
              primary: Colors.lightBlue,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8.0),
              ),
            ),
          ), */
          decoration: pageDecoration,
        ),
      ],
      onDone: () => _onIntroEnd(context),
      //onSkip: () => _onIntroEnd(context), // You can override onSkip callback
      showSkipButton: true,
      skipFlex: 0,
      nextFlex: 0,
      //rtl: true, // Display as right-to-left
      skip: Text(
        "Skip",
        style: TextStyle(color: Colors.black),
      ),
      next: const Icon(
        Icons.arrow_forward,
        color: Colors.black,
      ),
      done: Text("Get started", style: TextStyle(color: Colors.black)),

      controlsMargin: const EdgeInsets.all(16),
      controlsPadding: kIsWeb
          ? const EdgeInsets.all(12.0)
          : const EdgeInsets.fromLTRB(8.0, 4.0, 8.0, 4.0),
      dotsDecorator: const DotsDecorator(
        activeColor: Colors.black,
        size: Size(10.0, 10.0),
        color: Colors.black,
        activeSize: Size(22.0, 10.0),
        activeShape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(25.0)),
        ),
      ),
    );
  }
}
