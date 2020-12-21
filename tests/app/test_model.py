from app import model

lang_clf = model.LangClassifier()


def test_predict_runs():
    # just a smoke test
    pred = lang_clf.predict("this is a test!")
    assert pred
