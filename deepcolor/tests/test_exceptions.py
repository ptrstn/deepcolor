from deepcolor.exceptions import CaffeNotFoundError


def test_caffe_not_found_error():
    exception = CaffeNotFoundError()

    assert "Caffe is not installed. Unable to colorize picture." in str(exception)
    assert "https://caffe.berkeleyvision.org/installation.html" in str(exception)

    exception = CaffeNotFoundError("Some extra text")

    assert "Some extra text" in str(exception)
    assert "Caffe is not installed. Unable to colorize picture." in str(exception)
    assert "https://caffe.berkeleyvision.org/installation.html" in str(exception)
