from backend.app import summarize_with_llama


def test_summary_format():
    # Test for a typical paper summary
    sample_text = "This is a sample paper about Alzheimer's disease and its effects on the human brain..."
    summary = summarize_with_llama(sample_text)
    assert isinstance(summary, str), "Summary should be a string."
   


def test_empty_input():
    # Test with empty input
    summary = summarize_with_llama("")
    assert isinstance(summary, str), "Summary should be a string."
    assert summary == "", "Empty input should return an empty summary."
