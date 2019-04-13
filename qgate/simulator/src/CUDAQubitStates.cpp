#include "DeviceTypes.h"
#include "CUDAQubitStates.h"
#include "CUDAGlobals.h"

#include <string.h>
#include <algorithm>

using namespace qgate_cuda;
using qgate::Qone;
using qgate::Qtwo;


template<class real>
CUDAQubitStates<real>::CUDAQubitStates() {
    if (sizeof(real) == sizeof(float))
        prec_ = qgate::precFP32;
    else
        prec_ = qgate::precFP64;
    mchunk_ = NULL;
}

template<class real>
CUDAQubitStates<real>::~CUDAQubitStates() {
    deallocate();
}

template<class real>
void CUDAQubitStates<real>::allocate(int nLanes) {
    nLanes_ = nLanes;
    int po2idx = nLanes + (sizeof(DeviceComplex) / 8) + 3;
    mchunk_ = cudaMemoryStore.allocate(po2idx);
    devPtr_ = mchunk_->getMultiChunkPtr<DeviceComplex>();
}

template<class real>
void CUDAQubitStates<real>::deallocate() {
    if (mchunk_ != NULL)
        cudaMemoryStore.deallocate(mchunk_);
    mchunk_ = NULL;
}

template class CUDAQubitStates<float>;
template class CUDAQubitStates<double>;
