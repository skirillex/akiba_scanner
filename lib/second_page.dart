import 'package:flutter/material.dart';
import 'package:akiba_scanner/page_scaffold.dart';

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return PageScaffold(
      title: 'Second Page',
      body: Center(
        child:
        Text('Second Page', style: Theme.of(context).textTheme.headline4),
      ),
    );
  }
}