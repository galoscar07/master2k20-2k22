#include "HeapTracer.hpp"

HeapTracer::HeapTracer ()
{
	CheckPoint ();
}

HeapTracer::~HeapTracer ()
{
}

void HeapTracer::CheckPoint (void)
{
	_CrtMemCheckpoint (&mState);
}

void HeapTracer::Dump (void)
{
	_CrtMemDumpAllObjectsSince(&mState);
}