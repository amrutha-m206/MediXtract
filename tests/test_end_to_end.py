from backend.app import perform_search, summarize_with_llama


def test_end_to_end_flow():
    
    results = perform_search("alzheimer")
    assert len(results) > 0  #

  
    text = results[0].get("text_chunk", "")
    assert len(text.strip()) > 0 
    summary = summarize_with_llama(text[:1000])  
    assert len(summary.strip()) > 0  
