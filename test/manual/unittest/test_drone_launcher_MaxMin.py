import pytest, os, sys, flask
from unittest.mock import MagicMock, call

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/../../python")

import python.dronelauncher_python


app = flask.Flask(__name__)


@pytest.fixture()
def self():
    self = python.dronelauncher_python
    return self


def test_function_max_pitch(self):
    # GIVEN
    self.encoders_ready = 1
    app_client = self.app.test_client()
    self.rc = MagicMock()
    self.rc.ReadEncM1.return_value = (1, -1.5, 2)
    self.rc.ReadBuffers.return_value = (0, 0, 0x80)

    # WHEN
    response = app_client.post('/app_max_pitch', content_type='multipart/form-data',
                               data={'pitch_position': '90'})

    # THEN
    assert response.status_code == 204
    calls = [call(128, 7000, 355001.5, 1), call(128, 0, 0, 0)]
    self.rc.SpeedDistanceM1.assert_has_calls(calls)
    assert self.rc.SpeedDistanceM1.call_count == 2


def test_function_min_pitch(self):
    # GIVEN
    self.encoders_ready = 1
    app_client = self.app.test_client()
    self.rc = MagicMock()
    self.rc.ReadEncM1.return_value = (1, 3, 2)
    self.rc.ReadBuffers.return_value = (0, 0, 0x80)

    # WHEN
    response = app_client.post('/app_min_pitch', content_type='multipart/form-data',
                               data={'pitch_position': '111'})

    # THEN
    assert response.status_code == 204
    calls = [call(128, -7000, 3, 1), call(128, 0, 0, 0)]
    self.rc.SpeedDistanceM1.assert_has_calls(calls)
    assert self.rc.SpeedDistanceM1.call_count == 2


def test_function_max_lift(self):
    # GIVEN
    self.encoders_ready = 1
    app_client = self.app.test_client()
    self.rc = MagicMock()
    self.rc.ReadEncM1.return_value = (2, 7, 3)
    self.rc.ReadBuffers.return_value = (0, 0, 0x81)

    # WHEN
    response = app_client.post('/app_max_lift', content_type='multipart/form-data',
                               data={'lift_position': '450'})

    # THEN
    assert response.status_code == 204
    calls = [call(129, 420, 18993, 1), call(129, 0, 0, 0)]
    self.rc.SpeedDistanceM1.assert_has_calls(calls)
    assert self.rc.SpeedDistanceM1.call_count == 2


def test_function_min_lift(self):
    # GIVEN
    self.encoders_ready = 1
    app_client = self.app.test_client()
    self.rc = MagicMock()
    self.rc.ReadEncM1.return_value = (7, -8, 1)
    self.rc.ReadBuffers.return_value = (0, 0, 0x81)

    # WHEN
    response = app_client.post('/app_min_lift', content_type='multipart/form-data',
                               data={'lift_position': '80'})

    # THEN
    assert response.status_code == 204
    calls = [call(129, 420, 8, 1), call(129, 0, 0, 0)]
    self.rc.SpeedDistanceM1.assert_has_calls(calls)
    assert self.rc.SpeedDistanceM1.call_count == 2


def test_function_pitch_position_encoders_not_ready(self):
    # GIVEN
    self.encoders_ready = 0

    # WHEN
    returnValue = self.function_min_pitch()

    # THEN
    assert returnValue == ('', 403)


def test_function_lift_position_encoders_not_ready(self):
    # GIVEN
    self.encoders_ready = 0

    # WHEN
    returnValue = self.function_max_lift()

    # THEN
    assert returnValue == ('', 403)





