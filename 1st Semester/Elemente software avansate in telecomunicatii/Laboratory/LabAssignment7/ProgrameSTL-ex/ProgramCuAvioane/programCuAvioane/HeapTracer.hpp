#include "crtdbg.h"

class HeapTracer
{
public:
	HeapTracer ();
	~HeapTracer ();

	void CheckPoint (void);
	void Dump (void);

private:
	 _CrtMemState mState;
};