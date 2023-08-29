from sudoku_ocr.image import Image


class TestImage:
    def test_show(self, mocker) -> None:  # type: ignore
        mocker_imshow = mocker.patch("sudoku_ocr.image.imshow")
        mocker_waitKey = mocker.patch("sudoku_ocr.image.waitKey")
        image = Image()
        image.show()
        assert mocker_imshow.called
        assert mocker_waitKey.called
