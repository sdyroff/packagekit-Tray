#!/usr/bin/env python

from distutils.core import setup
setup(name='updateNotifier',
		version='0.0.1',
		scripts=['updateNotifier'],
		data_files=[('share/icons/hicolor/scalable/apps', ['updates_active.svg','updates_inactive.svg'])]
      )

